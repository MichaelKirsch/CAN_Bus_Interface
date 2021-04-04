import can

class CanCommunicator:
    def __init__(self):
        self.bus = can.interface.Bus()
        self.listener = can.BufferedReader()
        self.current_can_message = ""
        pass

    def __del__(self):
        self.listener.stop();

    def RetreiveMessage(self):
        x = self.listener.get_message(timeout=0.1)
        if x is not None:
            return x
        return ""

    def SendFrame(self,id,array):
        msg = can.Message(arbitration_id=id,
                          data=array,
                          is_extended_id=True)
        try:
            self.bus.send(msg)
            return False
        except can.CanError:
            return True

    def ListenForFrame(self):
        pass




class CoutCommunication:
    def __init__(self):
        print("Cout Communication started")
        pass

if __name__ == '__main__':
    c_com = CoutCommunication()
    can_com = CanCommunicator()

    while True:
        can_com.ListenForFrame()
