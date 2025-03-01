import unittest
#set transparency to true
transparent = True

#set is_cube to false
is_cube = False

#set glass to false
glass = False

colliders = []

#set values of the skeleton
bones = [{'name':'body','pivot':[0.0, 0.0, 0.0],'vertices':[[-0.25, 0.375, -0.125, -0.25, 1.125, -0.125, 0.25, 1.125, -0.125, 0.25, 0.375, -0.125], [0.25, 0.375, 0.125, 0.25, 1.125, 0.125, -0.25, 1.125, 0.125, -0.25, 0.375, 0.125], [-0.25, 1.125, -0.125, -0.25, 1.125, 0.125, 0.25, 1.125, 0.125, 0.25, 1.125, -0.125], [0.25, 0.375, -0.125, 0.25, 0.375, 0.125, -0.25, 0.375, 0.125, -0.25, 0.375, -0.125], [0.25, 0.375, -0.125, 0.25, 1.125, -0.125, 0.25, 1.125, 0.125, 0.25, 0.375, 0.125], [-0.25, 0.375, 0.125, -0.25, 1.125, 0.125, -0.25, 1.125, -0.125, -0.25, 0.375, -0.125]],'tex_coords':[[0.03333333333333333, 0.0, 0.03333333333333333, 0.75, 0.1, 0.75, 0.1, 0.0], [0.13333333333333333, 0.0, 0.13333333333333333, 0.75, 0.2, 0.75, 0.2, 0.0], [0.03333333333333333, 0.75, 0.03333333333333333, 1.0, 0.1, 1.0, 0.1, 0.75], [0.1, 0.75, 0.1, 1.0, 0.16666666666666666, 1.0, 0.16666666666666666, 0.75], [0.1, 0.0, 0.1, 0.75, 0.13333333333333333, 0.75, 0.13333333333333333, 0.0], [0.0, 0.0, 0.0, 0.75, 0.03333333333333333, 0.75, 0.03333333333333333, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'head','pivot':[0.0, 1.125, 0.0],'vertices':[[-0.25, 1.125, -0.25, -0.25, 1.625, -0.25, 0.25, 1.625, -0.25, 0.25, 1.125, -0.25], [0.25, 1.125, 0.25, 0.25, 1.625, 0.25, -0.25, 1.625, 0.25, -0.25, 1.125, 0.25], [-0.25, 1.625, -0.25, -0.25, 1.625, 0.25, 0.25, 1.625, 0.25, 0.25, 1.625, -0.25], [0.25, 1.125, -0.25, 0.25, 1.125, 0.25, -0.25, 1.125, 0.25, -0.25, 1.125, -0.25], [0.25, 1.125, -0.25, 0.25, 1.625, -0.25, 0.25, 1.625, 0.25, 0.25, 1.125, 0.25], [-0.25, 1.125, 0.25, -0.25, 1.625, 0.25, -0.25, 1.625, -0.25, -0.25, 1.125, -0.25]],'tex_coords':[[0.26666666666666666, 0.0, 0.26666666666666666, 0.5, 0.3333333333333333, 0.5, 0.3333333333333333, 0.0], [0.4, 0.0, 0.4, 0.5, 0.4666666666666667, 0.5, 0.4666666666666667, 0.0], [0.26666666666666666, 0.5, 0.26666666666666666, 1.0, 0.3333333333333333, 1.0, 0.3333333333333333, 0.5], [0.3333333333333333, 0.5, 0.3333333333333333, 1.0, 0.4, 1.0, 0.4, 0.5], [0.3333333333333333, 0.0, 0.3333333333333333, 0.5, 0.4, 0.5, 0.4, 0.0], [0.2, 0.0, 0.2, 0.5, 0.26666666666666666, 0.5, 0.26666666666666666, 0.0]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg0','pivot':[-0.125, 0.375, 0.25],'vertices':[[-0.25, 0.0, 0.125, -0.25, 0.375, 0.125, 0.0, 0.375, 0.125, 0.0, 0.0, 0.125], [0.0, 0.0, 0.375, 0.0, 0.375, 0.375, -0.25, 0.375, 0.375, -0.25, 0.0, 0.375], [-0.25, 0.375, 0.125, -0.25, 0.375, 0.375, 0.0, 0.375, 0.375, 0.0, 0.375, 0.125], [0.0, 0.0, 0.125, 0.0, 0.0, 0.375, -0.25, 0.0, 0.375, -0.25, 0.0, 0.125], [0.0, 0.0, 0.125, 0.0, 0.375, 0.125, 0.0, 0.375, 0.375, 0.0, 0.0, 0.375], [-0.25, 0.0, 0.375, -0.25, 0.375, 0.375, -0.25, 0.375, 0.125, -0.25, 0.0, 0.125]],'tex_coords':[[0.5, 0.375, 0.5, 0.75, 0.5333333333333333, 0.75, 0.5333333333333333, 0.375], [0.5666666666666667, 0.375, 0.5666666666666667, 0.75, 0.6, 0.75, 0.6, 0.375], [0.5, 0.75, 0.5, 1.0, 0.5333333333333333, 1.0, 0.5333333333333333, 0.75], [0.5333333333333333, 0.75, 0.5333333333333333, 1.0, 0.5666666666666667, 1.0, 0.5666666666666667, 0.75], [0.5333333333333333, 0.375, 0.5333333333333333, 0.75, 0.5666666666666667, 0.75, 0.5666666666666667, 0.375], [0.4666666666666667, 0.375, 0.4666666666666667, 0.75, 0.5, 0.75, 0.5, 0.375]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg1','pivot':[0.125, 0.375, 0.25],'vertices':[[0.0, 0.0, 0.125, 0.0, 0.375, 0.125, 0.25, 0.375, 0.125, 0.25, 0.0, 0.125], [0.25, 0.0, 0.375, 0.25, 0.375, 0.375, 0.0, 0.375, 0.375, 0.0, 0.0, 0.375], [0.0, 0.375, 0.125, 0.0, 0.375, 0.375, 0.25, 0.375, 0.375, 0.25, 0.375, 0.125], [0.25, 0.0, 0.125, 0.25, 0.0, 0.375, 0.0, 0.0, 0.375, 0.0, 0.0, 0.125], [0.25, 0.0, 0.125, 0.25, 0.375, 0.125, 0.25, 0.375, 0.375, 0.25, 0.0, 0.375], [0.0, 0.0, 0.375, 0.0, 0.375, 0.375, 0.0, 0.375, 0.125, 0.0, 0.0, 0.125]],'tex_coords':[[0.6333333333333333, 0.375, 0.6333333333333333, 0.75, 0.6666666666666666, 0.75, 0.6666666666666666, 0.375], [0.7, 0.375, 0.7, 0.75, 0.7333333333333333, 0.75, 0.7333333333333333, 0.375], [0.6333333333333333, 0.75, 0.6333333333333333, 1.0, 0.6666666666666666, 1.0, 0.6666666666666666, 0.75], [0.6666666666666666, 0.75, 0.6666666666666666, 1.0, 0.7, 1.0, 0.7, 0.75], [0.6666666666666666, 0.375, 0.6666666666666666, 0.75, 0.7, 0.75, 0.7, 0.375], [0.6, 0.375, 0.6, 0.75, 0.6333333333333333, 0.75, 0.6333333333333333, 0.375]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg2','pivot':[-0.125, 0.375, -0.25],'vertices':[[-0.25, 0.0, -0.375, -0.25, 0.375, -0.375, 0.0, 0.375, -0.375, 0.0, 0.0, -0.375], [0.0, 0.0, -0.125, 0.0, 0.375, -0.125, -0.25, 0.375, -0.125, -0.25, 0.0, -0.125], [-0.25, 0.375, -0.375, -0.25, 0.375, -0.125, 0.0, 0.375, -0.125, 0.0, 0.375, -0.375], [0.0, 0.0, -0.375, 0.0, 0.0, -0.125, -0.25, 0.0, -0.125, -0.25, 0.0, -0.375], [0.0, 0.0, -0.375, 0.0, 0.375, -0.375, 0.0, 0.375, -0.125, 0.0, 0.0, -0.125], [-0.25, 0.0, -0.125, -0.25, 0.375, -0.125, -0.25, 0.375, -0.375, -0.25, 0.0, -0.375]],'tex_coords':[[0.7666666666666667, 0.375, 0.7666666666666667, 0.75, 0.8, 0.75, 0.8, 0.375], [0.8333333333333334, 0.375, 0.8333333333333334, 0.75, 0.8666666666666667, 0.75, 0.8666666666666667, 0.375], [0.7666666666666667, 0.75, 0.7666666666666667, 1.0, 0.8, 1.0, 0.8, 0.75], [0.8, 0.75, 0.8, 1.0, 0.8333333333333334, 1.0, 0.8333333333333334, 0.75], [0.8, 0.375, 0.8, 0.75, 0.8333333333333334, 0.75, 0.8333333333333334, 0.375], [0.7333333333333333, 0.375, 0.7333333333333333, 0.75, 0.7666666666666667, 0.75, 0.7666666666666667, 0.375]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg3','pivot':[0.125, 0.375, -0.25],'vertices':[[0.0, 0.0, -0.375, 0.0, 0.375, -0.375, 0.25, 0.375, -0.375, 0.25, 0.0, -0.375], [0.25, 0.0, -0.125, 0.25, 0.375, -0.125, 0.0, 0.375, -0.125, 0.0, 0.0, -0.125], [0.0, 0.375, -0.375, 0.0, 0.375, -0.125, 0.25, 0.375, -0.125, 0.25, 0.375, -0.375], [0.25, 0.0, -0.375, 0.25, 0.0, -0.125, 0.0, 0.0, -0.125, 0.0, 0.0, -0.375], [0.25, 0.0, -0.375, 0.25, 0.375, -0.375, 0.25, 0.375, -0.125, 0.25, 0.0, -0.125], [0.0, 0.0, -0.125, 0.0, 0.375, -0.125, 0.0, 0.375, -0.375, 0.0, 0.0, -0.375]],'tex_coords':[[0.9, 0.375, 0.9, 0.75, 0.9333333333333333, 0.75, 0.9333333333333333, 0.375], [0.9666666666666667, 0.375, 0.9666666666666667, 0.75, 1.0, 0.75, 1.0, 0.375], [0.9, 0.75, 0.9, 1.0, 0.9333333333333333, 1.0, 0.9333333333333333, 0.75], [0.9333333333333333, 0.75, 0.9333333333333333, 1.0, 0.9666666666666667, 1.0, 0.9666666666666667, 0.75], [0.9333333333333333, 0.375, 0.9333333333333333, 0.75, 0.9666666666666667, 0.75, 0.9666666666666667, 0.375], [0.8666666666666667, 0.375, 0.8666666666666667, 0.75, 0.9, 0.75, 0.9, 0.375]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}]


class CowTestCase(unittest.TestCase):
    def test_transparency(self):
        self.assertTrue(transparent)

    def test_is_cube(self):
        self.assertFalse(is_cube)

    def test_glass(self):
        self.assertFalse(glass)

    def test_colliders(self):
        self.assertEqual(len(colliders), 0)

    def test_bones(self):
        self.assertIsInstance(bones, list)
        self.assertGreater(len(bones), 0)

        for bone in bones:
            self.assertIsInstance(bone, dict)
            self.assertIn('name', bone)
            self.assertIn('pivot', bone)
            self.assertIn('vertices', bone)
            self.assertIn('tex_coords', bone)
            self.assertIn('shading_values', bone)

            self.assertIsInstance(bone['name'], str)
            self.assertIsInstance(bone['pivot'], list)
            self.assertIsInstance(bone['vertices'], list)
            self.assertIsInstance(bone['tex_coords'], list)
            self.assertIsInstance(bone['shading_values'], list)

            self.assertEqual(len(bone['pivot']), 3)
            self.assertEqual(len(bone['vertices']), 6)
            self.assertEqual(len(bone['tex_coords']), 6)
            self.assertEqual(len(bone['shading_values']), 6)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
