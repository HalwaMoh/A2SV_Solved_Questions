class FrequencyTracker(object):

    def __init__(self):
        self.count = {}
        self.freqCount = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        oldFreq = self.count.get(number,0)
        newFreq = oldFreq + 1

        self.count[number] = newFreq

        if oldFreq > 0:
            self.freqCount[oldFreq] -= 1
            if self.freqCount[oldFreq] == 0:
                del self.freqCount[oldFreq]

        self.freqCount[newFreq] = self.freqCount.get(newFreq,0) + 1


    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number not in self.count:
            return

        oldFreq = self.count[number]
        newFreq = oldFreq - 1

        self.freqCount[oldFreq] -= 1
        if self.freqCount[oldFreq] == 0:
            del self.freqCount[oldFreq]

        if newFreq == 0:
            del self.count[number]
        else:
            self.count[number] = newFreq
            self.freqCount[newFreq] = self.freqCount.get(newFreq,0) + 1

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return frequency in self.freqCount
