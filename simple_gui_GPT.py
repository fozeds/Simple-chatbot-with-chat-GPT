
import PySimpleGUI as sg
from getpass import getuser as usuario
import openai


#This script uses the PySimpleGUI library, which is cross-platform, and the OpenAI API, 
#which is accessed through the openai library. Although PySimpleGUI does not run natively
#on Linux and is not recommended to use it with wine, you can look for other libraries 
#similar to PySimpleGUI that are compatible with Linux and can be used in your script.
class ChatGPT:
    def __init__(self):
        # Get the OpenAI API key from the user
        self.api_key = sg.popup_get_text("Please enter your OpenAI API Key")
        # Set the API key
        openai.api_key = self.api_key
        # Set the model to use
        self.model = "text-davinci-003"
        # Set the theme for the GUI
        sg.theme('Topanga')

    def gpt(self, text):
        """
        This method sends the text to the GPT-3 model and returns the generated response
        """
        try:
            response = openai.Completion.create(
                model=self.model,
                prompt=text,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            return response["choices"][0]["text"]
        except Exception as e:
            print(e)
            
    def run(self):
        """
        This method runs the GUI and handles the events
        """
        layout = [[sg.Text('Pergunte ao GPT', size=(40, 1))],
                  [sg.Output(size=(110, 20), font=('Helvetica 10'))],
                  [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
                   sg.Button('ENVIAR',key="SEND", button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                   sg.Button('SAIR',key="EXIT", button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

        # Create the window
        window = sg.Window('Simple Chat GPT', layout, font=('Helvetica', ' 15'), default_button_element_size=(8,2), use_default_focus=False,resizable=True,modal=True,location =(0,0)).finalize()
        a = "-=≡𓃑Ξ⁝𓏬⋮☰㊂☰⋮𓏬⁝Ξ𓃑≡=-"*5

        # Event loop
        while True:
            event, value = window.read()
            if event in (sg.WIN_CLOSED, 'EXIT'):
                break
            if event == 'SEND':
                query = value['-QUERY-'].rstrip()
                print(f'{usuario()} \N{SNOWMAN} {query}', flush=True)
                print(f"\n\n\n{a}\n{self.gpt(query)}",flush = True)
        # Close the window
        window.close()

if __name__ == "__main__":
    gpt_chatbot = ChatGPT()
    gpt_chatbot.run()