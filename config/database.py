import sqlite3
import time

class SQLighter:
      def __init__(self,database_file):
            self.connection = sqlite3.connect(database_file)
            self.cursor = self.connection.cursor()
      ## проверка человека в базе данных 
      def subscriber_exists(self,user_id):
            with self.connection:
                  result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
                  return bool(len(result))
            
      ## добавление юзера в базу данных   
      def add_user(self, user_id):
            with self.connection:
                  return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES(?)",(user_id,))    

      ## добавление и выбор ника по юзер ид        
      def username_exists(self,user_id):
            with self.connection:
                  result = self.cursor.execute("SELECT `user_name` FROM `users` WHERE `user_id` = ?", (user_id,))
                  return result.fetchone()      
      def updape_username(self, user_name, user_id):
            with self.connection:
                  return self.cursor.execute("UPDATE `users` SET `user_name` = ? WHERE `user_id` = ?",(user_id,user_name,))

      ## Проверка и регистрациия пользователя                 
      def get_singup(self,user_id):
            with self.connection:
                  result = self.cursor.execute("SELECT `singup` FROM `users` WHERE `user_id` = ? ",(user_id,)).fetchall()
                  for row in result:
                        singup = str(row[0])
                  return singup      
      def updape_singup(self, singup, user_id):
            with self.connection:
                  return self.cursor.execute("UPDATE `users` SET `singup` = ? WHERE `user_id` = ?",(user_id,singup,))                              
            
      ## Проверка и подписка пользователя на бот      

      def status_exists(self,user_id):
            with self.connection:
                  result = self.cursor.execute("SELECT `status` FROM `users` WHERE `user_id` = ?", (user_id,))
                  return result.fetchone()

      def updape_status(self, status, user_id):
            with self.connection:
                  return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?",(user_id,status,))            

      def updape_time_sub(self, user_id, time_sub):
            with self.connection:
                  return self.cursor.execute("UPDATE `users` SET `time_sub` = ? WHERE `user_id` = ?",(time_sub,user_id,))       
            
      def get_time_sub(self,user_id):
            with self.connection:
                  result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ? ",(user_id,)).fetchall()
                  for row in result:
                        time_sub = int(row[0])
                  return time_sub           
            
      def get_timesubstatus(self,user_id):
            with self.connection:
                  result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ? ",(user_id,)).fetchall()
                  for row in result:
                        time_sub = int(row[0])
                  if time_sub > int(time.time()):
                        return True
                  else:
                        return False              