from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Stream+")
app.geometry("400x400")


# Main login page
def loginPage():
  title = ctk.CTkLabel(app,
                       text=" ✮ Stream+ ",
                       fg_color="#18181a",
                       font=("Helvetica", 37),
                       anchor="w",
                       text_color="white")

  title.place(rely=0.01, relwidth=1, relheight=0.18) #Relative placement

  #the page switch at the top
  tabButton = ctk.CTkTabview(app,
                             fg_color="#18181a",
                             border_color=("#18181a"),
                             height=270,
                             width=270,
                             corner_radius=12)
  tabButton.add("Login")
  tabButton.add("SignUp")
  tabButton.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.7)

  loginTab = tabButton.tab("Login")
  loginLabel = ctk.CTkLabel(loginTab,
                            text="Login",
                            fg_color="#18181a",
                            font=("Helvetica", 35))
  loginLabel.place(
      rely=0.01, relx=0.5,
      anchor='n') # n means north so it centres horizontaly but not vertically
  global loginUsername
  loginUsername = ctk.CTkEntry(loginTab,
                               corner_radius=12,
                               placeholder_text="Enter Your Username.....",
                               height=45,
                               width=300)
  global loginPassword
  loginPassword = ctk.CTkEntry(loginTab,
                               placeholder_text="Enter Your Password.....",
                               height=45,
                               width=300,
                               corner_radius=12)
  loginUsername.place(relx=0.5, rely=0.2, anchor="n")
  loginPassword.place(relx=0.5, rely=0.4, anchor="n")
  loginButton = ctk.CTkButton(loginTab,
                              corner_radius=12,
                              text="Login",
                              height=45,
                              width=300,
                              command=checkLogin)
  loginButton.place(relx=0.5, rely=0.6, anchor="n")

  signupTab = tabButton.tab("SignUp") # copy pasting the login code
  signupLabel = ctk.CTkLabel(signupTab,
                             text="SignUp",
                             fg_color="#18181a",
                             font=("Helvetica", 35))
  signupLabel.place(
      rely=0.01, relx=0.5,
      anchor='n') # i used trial and error to get these relative positions :(

  global signupUsername
  signupUsername = ctk.CTkEntry(signupTab,
                                placeholder_text="Enter Your Username.....",
                                height=45,
                                width=300,
                                corner_radius=12)
  global signupPassword
  signupPassword = ctk.CTkEntry(signupTab,
                                corner_radius=12,
                                placeholder_text="Enter Your Password.....",
                                height=45,
                                width=300)
  signupUsername.place(relx=0.5, rely=0.2, anchor="n")
  signupPassword.place(relx=0.5, rely=0.4, anchor="n")
  signupButton = ctk.CTkButton(signupTab,
                               corner_radius=12,
                               text="SignUp",
                               height=45,
                               width=300,
                               command=createLogin)
  signupButton.place(relx=0.5, rely=0.6, anchor="n")

  global loginStatus
  loginStatus = ctk.CTkLabel(loginTab, text="", fg_color=None,font = ("Helvetica",23))
  loginStatus.place(relx=0.5, rely=0.8, anchor="n")


#debugged code ends here


def checkLogin(): # input validation
  checkValid = False
  admin = False
  if loginPassword.get() == "admin" and loginUsername.get() == "admin123":
    admin = True
  elif loginPassword.get() == "existing" and loginUsername.get() == "existing":
    checkValid = True #compare on database to check if user exists
    # COmplete this when you learn to read database
  elif loginPassword.get() == "" and loginUsername.get() == "":
    loginStatus.configure(text="Enter your Username and Password",
                          text_color="white")
  else:
    loginStatus.configure(text="Incorrect Username or Password",
                          text_color="#ff0000")

  displayPage(checkValid, admin)


def createLogin():
  #write login details to database user
  pass


def customer():
  customerPage = ctk.CTkToplevel(app)
  customerPage.title("Customer Portal")

  pass


def staff():
  staffPage = ctk.CTkToplevel(app)
  staffPage.title("Customer Portal")
  pass


def displayPage(checkValid, admin):
  if checkValid == True:
    customer()
  elif admin == True:
    staff()
  pass


def main():
  loginPage()

  pass


main()

app.mainloop()
