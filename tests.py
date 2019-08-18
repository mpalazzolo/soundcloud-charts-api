from soundcloudcharts import SoundCloudCharts
import unittest


class TestSoundCloud(unittest.TestCase):

    def test_client_id(self):
        result = sc.get_client_id()
        self.assertTrue(type(result) == str)
        self.assertEqual(len(result), 32)

    def test_chart(self):
        limit = 50
        result = sc.get_chart(limit=limit)
        self.assertEqual(len(result['collection']), limit)
        self.assertEqual(result['genre'], 'soundcloud:genres:all-music')


if __name__ == '__main__':

    sc = SoundCloudCharts()
    unittest.main()
