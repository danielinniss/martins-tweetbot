import unittest
import tweet_shit
import random_lines
import os

class TestTweetShit(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_text_file.txt'
        f = open(self.filename, 'w+')
        f.write(self.text_for_file())
        f.close()

    def tearDown(self):
        os.remove(self.filename)

    def test_get_line(self):
        expected = 'minas> :V\n'
        line = random_lines._get_line(self.filename, 5)
        self.assertEqual(line[1], expected)

    def text_for_file(self):
        return ("#scrapheap_20100720.log:[16:10:24] <minas> oh silly me\n"
                 "#scrapheap_20100720.log:[16:10:29] <minas> of course you haven't\n"
                 "#scrapheap_20100720.log:[16:10:31] *** minas was kicked by MaZ- (MaZ-)\n"
                 "#scrapheap_20100720.log:[16:10:31] *** Joins: minas (hurf@coldfront-4A0FD661.zone2.bethere.co.uk)\n"
                 "#scrapheap_20100720.log:[16:10:32] <minas> :V\n"
                 "#scrapheap_20100720.log:[16:11:16] <minas> hurr\n"
                 "#scrapheap_20100720.log:[16:11:36] <minas> terrible puns best puns\n"
                 "#scrapheap_20100720.log:[16:12:28] <minas> well it's spelled wrong anyway\n"
                 "#scrapheap_20100720.log:[16:12:39] <minas> TWO T'S IN MATTRESS\n"
                 "#scrapheap_20100720.log:[16:12:59] <minas> pedant4lyfe\n"
                 "#scrapheap_20100720.log:[16:13:25] <minas> yes i do plan on having a penis for life\n"
                 "#scrapheap_20100720.log:[16:13:43] <minas> (in ur mother)\n"
                 "#scrapheap_20100720.log:[16:13:52] <minas> ho ho\n"
                 "#scrapheap_20100720.log:[16:14:57] <minas> it's like reading plato only with more cock jokes\n"
                 "#scrapheap_20100720.log:[16:18:31] <minas> time to make a hilarious alien swarm map\n"
                 "#scrapheap_20100720.log:[16:18:38] <spiralJunkie> minas you can MAKE MAPS?\n"
                 "#scrapheap_20100720.log:[16:18:42] <minas> yus\n"
                 "#scrapheap_20100720.log:[16:18:49] <minas> http://developer.valvesoftware.com/wiki/Swarm_TileGen\n"
                 "#scrapheap_20100720.log:[16:18:56] <minas> :|\n"
                 "#scrapheap_20100720.log:[16:19:01] <minas> GET\n"
                 "#scrapheap_20100720.log:[16:19:02] <minas> OUT\n"
                 "#scrapheap_20100720.log:[16:19:04] <spiralJunkie> I'm thinking of making an area where there are many aliens and minas dies 3% of the way in")

if __name__ == '__main__':
    unittest.main()
