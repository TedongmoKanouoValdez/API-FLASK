# import customtkinter

# def get_pokemon(): 
#     print("requete vers l'api pokemon")

# customtkinter.set_appearance_mode("red")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="button", command=get_pokemon)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# app.mainloop()


# import customtkinter

# customtkinter.set_appearance_mode("Dark") 
# customtkinter.set_default_color_theme("green")  

# class ButonAPP(customtkinter.CTk):
   
#     def __init__(self):
#         super().__init__()
#         self.title("Mon application #1")
#         self.geometry(f"{1100}x{580}")
        
#         self.grid_columnconfigure((1, 2, 3), weight=1 )
#         self.grid_rowconfigure((0, 1, 2), weight=1 )
        
#         self.principal_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0) 
#         self.principal_frame.grid(row=1, column=3, rowspan=4)
        
#         self.button = customtkinter.CTkButton(master=self.principal_frame, text="Cliquez ici", command = self.say_hello)
#         self.button.grid(row=3, column=1)
       
#     def say_hello(self):
#         print("Hello World")


# if __name__ == "__main__":
#     mon_instance = ButonAPP()    
#     mon_instance.mainloop()

from openai import OpenAI
client = OpenAI(api_key="KEY Api")

import customtkinter
import requests
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")  
class requestsAPP(customtkinter.CTk):
    
    user_input = ""
    historique_conversation = [{'role': 'system', 'content': 'Tu repondras par la négation à toutes les questions que ton interlocuteur te pose'}]
   
    def __init__(self):
        super().__init__()
        self.title("Mon application #1")
        self.geometry(f"{1100}x{580}")
        
        #créer une grille de 3 lignes et 3 colonnes
        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)
    
    
        # partie bouton
        self.buton_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.buton_frame.grid(row=0, column=1)
        
        self.button = customtkinter.CTkButton(master=self.buton_frame, text="Cliquez ici", command=self.update_user_input)
        self.button.grid()
        
        # partie champs texte
        self.text_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0)
        self.text_frame.grid(row=0, column=0)
        
        self.user_text = customtkinter.CTkEntry(master=self.text_frame, height=10, width=800)
        self.user_text.grid()
        
        
        # partie resultat
        self.result_frame = customtkinter.CTkFrame(self, width=8000, corner_radius=0)
        self.result_frame.grid(row=1, column=0)
        
        self.result_box = customtkinter.CTkTextbox(master=self.result_frame, height=400, width=800)
        self.result_box.configure(state="disabled")
        self.result_box.grid(sticky="nsew" )
       
    def update_user_input(self):

        self.result_box.configure(state="normal")
        self.result_box.delete("0.0", "end")    
        # récupere le texte de l'utilisateur
        t = self.user_text.get()
        self.user_input = t
        self.historique_conversation += [{'role': 'user', 'content': self.user_input}]
        print(self.historique_conversation)
        # appeler l'api pokemon
        try:
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= self.historique_conversation
            )
            response = completion.choices[0].message.content
            self.historique_conversation += [{'role': 'assistant', 'content': response}]
            self.result_box.configure(state="normal")
            self.result_box.insert("0.0", response)
            self.result_box.configure(state="disabled")
            print( response )
        except Exception as e:
            print(e);
            self.result_box.configure(state="normal")
            self.result_box.insert("0.0", "Erreur lors de la requete")
            self.result_box.configure(state="disabled")
        
    def update_conversation_history(self):
        # Affiche la conversation complète
        for message in self.historique_conversation:
            role = message['role']
            content = message['content']
            self.result_box.configure(state="normal")
            self.result_box.insert("end", f"{role}: {content}\n")
            self.result_box.configure(state="disabled")
 
if __name__ == "__main__":
    mon_instance = requestsAPP()    
    mon_instance.mainloop()
 