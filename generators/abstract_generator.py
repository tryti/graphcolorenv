class AbstractGraphGenerator:

    def next(self):
        """
        Returns a new graph and its chromatic number.
        Returns:
            g (NetworkX.Graph) - NetworkX graph with
            c (int) - Chromatic number of c
        """
        raise NotImplementedError

    def seed(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError
