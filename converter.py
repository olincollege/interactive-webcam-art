'''
Use body tracking values to generate useable values for the 
artwork parameters
landmark_points: The list of landmark points that are to be refrenced
by the class Convert
bodypart_number: The index number of the bodypart which will be used
'''
class Convert:
    def __init__(self, landmark_points, bodypart_number):
        self.bodypart_number = bodypart_number
        self.landmark = str(landmark_points[bodypart_number])

    def depth(self):
        return int(self.landmark[6])

    #Experimental code for further development

    # def xcoordinate(self):
    #     return self.landmark[6:8]

    # def ycoordinate(self):
    #     return self.landmark[28:30]

    # def rgb(self, axis):
    #     '''
    #     Axis: 'x' or 'y' input
    #     '''
    #     if axis == 'x':
    #         return int(self.xcoordinate()) * 2
    #     if axis == 'y':
    #         return int(self.ycoordinate()) * 2