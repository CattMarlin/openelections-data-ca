#!/usr/bin/env python3

import csv
import glob
import os
import pandas
import pytest
import re
import unittest


columns = ['candidate', 'county', 'district', 'office', 'votes']


@pytest.mark.parametrize("year,date,election_type", [
    ("2014", "0603", "primary"),
    ("2014", "1104", "general"),
    ("2015", "0317", "special__primary"),
    ("2015", "0519", "special__general"),
    ("2016", "0405", "special__primary"),
    ("2016", "0607", "primary"),
    ("2016", "1108", "general"),
    ("2017", "0404", "special__primary"),
    ("2017", "0606", "special__general"),
    ("2017", "1003", "special__primary"),
])
def test_data(year, date, election_type):
    state_file = '{0}/{0}{1}__ca__{2}.csv'.format(
        year, date, election_type)
    state_data = pandas.read_csv(state_file, na_values='').fillna('')
    state_data = state_data[state_data.votes != 0]

    for county_file in sorted(glob.glob('{0}/{0}{1}__ca__{2}__*__precinct.csv'.format(year, date, election_type))):
        county_data = pandas.read_csv(county_file, na_values='').fillna('')

        # Each county file should only contain a single county.
        assert len(county_data.drop_duplicates(
            ['county']).county.values) == 1

        county = county_data.drop_duplicates(['county']).county.values[0]
        county_data = county_data[columns].groupby(
            columns[:-1]).sum()
        state_cmp = state_data[state_data.county == county][
            columns].groupby(columns[: -1]).sum()

        assert state_cmp.to_dict()['votes'] == county_data.to_dict()[
            'votes'], '%s failed' % county


class FileFormatTests(unittest.TestCase):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    def test_format(self):
        regex_non_whitespace = re.compile(r"\S")
        regex_consecutive_space = re.compile(r"\s{2,}")
        regex_non_alphanumeric = re.compile(r"\w")

        for csv_file in FileFormatTests.__get_csv_files():
            short_path = csv_file.strip(FileFormatTests.root_path)
            with self.subTest(msg=f"{short_path}"):
                with open(csv_file, "r") as csv_data:
                    reader = csv.reader(csv_data)

                    required_headers = set(FileFormatTests.__get_expected_headers(csv_file))
                    headers = next(reader)

                    # Verify that the header does not contain any empty entries.
                    self.assertNotIn("", headers, f"File {short_path} has an empty column header.")

                    # Verify that the header contains the required entries.
                    self.assertTrue(required_headers.issubset(headers), f"File {short_path} has header: {headers}, "
                                                        f"which is missing: {required_headers.difference(headers)}.")

                    # An "unknown" header is not useful.
                    self.assertNotIn("unknown", [x.strip().lower() for x in headers], f"File {short_path} has an "
                                                                                      f"'unknown' header: {headers}.")

                    for row in reader:
                        # Verify that each row has the expected number of entries.
                        self.assertEqual(len(headers), len(row), f"File {short_path} has header {headers}, but row "
                                                                 f"{reader.line_num} is {row}.")
                        row_has_content = False
                        for entry in row:
                            row_has_content |= (regex_non_whitespace.search(entry) is not None)

                            # Verify that there is no leading or trailing whitespace.  Using assertFalse instead of
                            # assertEqual provides a slightly better failure message.
                            has_leading_trailing_space = entry.strip() != entry
                            self.assertFalse(has_leading_trailing_space, f"File {short_path} has leading or trailing "
                                                                   f"whitespace in row {reader.line_num}: {row}.")

                            # Verify that there are no consecutive whitespace characters.
                            self.assertNotRegex(entry, regex_consecutive_space, f"File {short_path} contains "
                                                                                f"consecutive whitespace characters "
                                                                                f"in row {reader.line_num}: {row}.")

                            # Verify that there are no line breaks in the row (sometimes occurs in between quotes).
                            self.assertNotIn("\n", entry, f"File {short_path} has a newline character in row "
                                                          f"{reader.line_num}: {row}.")

                            # Verify that the entry does not consist only of non-alphanumeric characters.
                            if entry != "":
                                self.assertRegex(entry, regex_non_alphanumeric, f"File {short_path} has an entry of "
                                                                                f"only non-alphanumeric characters in"
                                                                                f" row {reader.line_num}: {row}.")

                        # Verify that the row has actual content.
                        self.assertTrue(row_has_content, f"File {short_path} row {reader.line_num} is empty.")

    @staticmethod
    def __get_csv_files():
        data_folders = glob.glob(os.path.join(FileFormatTests.root_path, "[0-9]" * 4))
        for data_folder in data_folders:
            for root, dirs, files in os.walk(data_folder):
                for file in files:
                    if file.lower().endswith(".csv"):
                        yield os.path.join(root, file)

    @staticmethod
    def __get_expected_headers(csv_file):
        if csv_file.endswith("precinct.csv"):
            return ["county", "precinct", "office", "district", "party", "candidate", "votes"]
        else:
            return ["county", "office", "district", "party", "candidate", "votes"]
