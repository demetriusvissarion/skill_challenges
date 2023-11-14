import math

## Exercise
class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.contents_tracker = ''

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        if self.title == None or len(self.title) <= 0 or self.contents == None or len(self.contents) <= 0:
            raise Exception("Invalid entry, 'title' and 'contents' must have at least one character.")
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        if self.title == None or len(self.title) <= 0 or self.contents == None or len(self.contents) <= 0:
            raise Exception("Invalid entry, 'title' and 'contents' must have at least one character.")
        if self.contents:
            count = 1
            for i in range(0, len(self.contents)):
                if self.contents[i] == " ":
                    count += 1
            return count
        else:
            return 0

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if self.title == None or len(self.title) <= 0 or self.contents == None or len(self.contents) <= 0:
            raise Exception("Invalid entry, 'title' and 'contents' must have at least one character.")
        if len(self.contents) > 0:
            words = 1
            for i in range(0, len(self.contents)):
                if self.contents[i] == " ":
                    words += 1
            minutes = math.ceil(words / wpm)
            return minutes

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        # minutes_to_read_all = self.reading_time(wpm)
        # print(wpm * minutes)

        if len(self.contents_tracker) > 0:
            result = self.contents_tracker.split()
            self.contents_tracker = ''
        else:
            self.contents_tracker = self.contents
            result = self.contents_tracker.split()[:(wpm * minutes)]
            self.contents_tracker = ' '.join(self.contents_tracker.split()[(wpm * minutes):])

        return ' '.join(result)
    


calculator = DiaryEntry("Latin Lesson", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras maximus neque ut enim finibus mattis. Pellentesque finibus, neque nec viverra varius, purus neque lobortis enim, vel posuere urna quam quis lorem. Quisque blandit dui sit amet ligula tempor sagittis. Etiam eu vulputate nunc, ut tempor velit. Morbi facilisis pellentesque ex, vitae feugiat eros pellentesque sit amet. Donec in ante aliquet, tincidunt dui sit amet, accumsan dolor. Cras ultrices nisl nunc, quis suscipit est auctor id. Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci. Morbi ut convallis est. Maecenas sed metus nulla. Maecenas rhoncus arcu non vulputate placerat. Suspendisse posuere tincidunt odio, sodales tincidunt velit porttitor a. Vivamus sit amet lorem ac enim dapibus consectetur. Ut laoreet lobortis vestibulum. Nunc ac porta magna, ac scelerisque elit. Donec viverra, enim eget gravida ornare, sapien enim accumsan sapien, id volutpat tellus sem eget felis. Aliquam erat volutpat. Fusce porta sem eget nibh ullamcorper, eu tristique orci feugiat. Vestibulum eros enim, maximus vel dolor a, eleifend sollicitudin mauris. Etiam vel mollis massa. Fusce condimentum lacinia ante, et vulputate sem fringilla eu. Integer fermentum tristique metus et viverra. Nam volutpat dolor vel facilisis porta. Pellentesque aliquet quis elit sit amet fringilla. Nulla rhoncus leo eu velit tincidunt, mattis venenatis magna hendrerit. Sed non euismod tellus, vel faucibus magna. Sed sit amet lectus luctus metus condimentum suscipit sed sed libero. Donec a sapien felis. Vivamus condimentum quis nulla in ultrices. Vestibulum facilisis nibh dolor, ac convallis massa volutpat at. Donec tincidunt interdum ligula, eu elementum sem egestas quis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed porta suscipit odio quis dignissim. Pellentesque tincidunt convallis tempor. Maecenas mollis mattis lacus, in ultricies arcu lacinia ac.")
result = calculator.reading_chunk(50, 1)
print(result)
result2 = calculator.reading_chunk(50, 1)
print(result2)
result3 = calculator.reading_chunk(50, 1)
print(result3)