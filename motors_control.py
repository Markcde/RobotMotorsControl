   class Robot:
       def __init__(self):
           self.speed = 0

       def set_speed(self, speed):
           self.speed = speed
           print(f"Скорость установлена на {self.speed}")

       def stop(self):
           self.speed = 0
           print("Робот остановлен")

   if __name__ == "__main__":
       robot = Robot()
       robot.set_speed(5)
       robot.stop()
   
