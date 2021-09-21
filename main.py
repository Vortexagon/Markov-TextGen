import random

class MarkovChain:
    def __init__(self, data):
        # A 2D dictionary of values. graph['E']['F'] will return the number of times EF appeared.
        graph = dict()

        # The character we just left.
        prev_char = None
        
        for char in data:
            # Initialise the character's entry before we try to use it.
            if char not in graph.keys():
                graph[char] = dict()
                
            if prev_char is not None:
                # Initialise the character's entry before we try to use it.
                if char not in graph[prev_char].keys():
                    graph[prev_char][char] = 0
                    
                graph[prev_char][char] += 1
            prev_char = char
            
        self.graph = graph

    def walk_from_len(self, start, length):
        """
        Recursively generates a walk, starting at `start`, and of maximum length `length`.
        It's maximum length and not exact length, because sometimes we may visit a node that
        has no paths back to any other nodes. We would need to terminate the generation at
        this stage.
        """
        start_node = self.graph[start]
        
        if len(start_node.keys()) == 0:
            return start
        
        # start_node.items() returns pairs of (node, number of times visited).
        # If EF exists in the sequence 5 times, we'll find a ('F', 5) tuple when start_node == 'E'.
        # random.choices takes a list of choices and a list of weights, and gives weighted random outputs.
        # These zipping and unpacking operations turn something like:
        #
        #     [('A', 4), ('B', 8), ('C', 2)]
        #
        # Into:
        #
        #     ('A', 'B', 'C'), (4, 8, 2)
        #
        # Ready for random.choices() to work correctly. Since random.choices() returns a list, we
        # extract the first element using [0].
        pick = random.choices(*zip(*start_node.items()))[0]

        if length == 1:
            return pick

        return start + self.walk_from_len(pick, length- 1)


##### Demo. Any walk of the below sequence should try to imitate the long stretches of 'DDD...'



chain = MarkovChain("The quick brown fox jumped over the lazy dog.")

start_node = "T"
max_length = 50

print(f"Generating Markov Chain.\nMax Length: {max_length}\nStart at: {start_node}\n")
print(chain.walk_from_len(start_node, max_length))
