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
   import time

   def smooth_speed_change(robot, target_speed, duration):
       initial_speed = robot.speed
       step = (target_speed - initial_speed) / (duration * 10)  # 10 шагов в секунду
       for _ in range(duration * 10):
           initial_speed += step
           robot.set_speed(initial_speed)
           time.sleep(0.1)
      
