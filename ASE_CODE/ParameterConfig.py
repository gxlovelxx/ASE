class ParameterConfig(object):
    #def __init__(self,ParameterName,Description,Unit,SignBit,Lsb,Msb,BitLength,StartWord,EndWord,WordIncrement,InitialFrame	,FrameIncrement,LsbRes,DataType):
    def __init__(self, ParameterName = "",Lsb = 0, Msb = 0,StartWord = 0, EndWord = 0,WordIncrement = 0, InitialFrame = 0, FrameIncrement = 0, LsbRes = 0, DataType = "",Bias = 0):
        self.ParameterName = ParameterName
        self.Lsb = Lsb
        self.Msb = Msb
        self.StartWord = StartWord
        self.EndWord = EndWord
        self.WordIncrement = WordIncrement
        self.InitialFrame = InitialFrame
        self.FrameIncrement = FrameIncrement
        self.LsbRes = LsbRes
        self.DataType = DataType
        self.Bias = Bias

