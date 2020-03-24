import unittest
from unittest.mock import patch, mock_open
import urllib.request
import make_request


class MakeRequestTest(unittest.TestCase):

    def test_call_nooa(self):
        with patch('urllib.request.urlopen') as cm:
            make_request.call_nooa(offset=1, token='super_secret_token')
        cm.assert_called_once()

        expected_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1000&offset=1'

        call_args = cm.call_args[0][0]
        self.assertTrue(isinstance(call_args, urllib.request.Request))
        self.assertEqual(expected_url, call_args.full_url)
        self.assertEqual('super_secret_token', call_args.headers['Token'])

    def test_write_result(self):
        data = b"{\"testKey\": \"testValue\"}"

        with patch("builtins.open", mock_open(read_data=data)) as mf:
            make_request.write_result(data, "dummy.json")

        mf.assert_called_once_with('./data/dummy.json', 'wb')
        mf.return_value.write.assert_called_once_with(data)
