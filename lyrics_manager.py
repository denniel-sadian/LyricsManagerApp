#! python3
# January 9, 2018

from tkinter import *
from tkinter import ttk, font, messagebox
from tkinter.colorchooser import askcolor
from shelve import open as _open
from os.path import exists
from about_dialog import AboutDialog


class LyricsManager(ttk.Notebook):

    def __init__(self, master, **kwargs):
        ttk.Notebook.__init__(self, master, **kwargs)
        self.root = master
        # shelve initialization
        if exists('lyrics_manager.dat'):
            self.app_data = _open('lyrics_manager')
        else:
            self.app_data = _open('lyrics_manager')
            self.app_data['font'] = 'Segoe Print'
            self.app_data['base_color'] = 'green'
            self.app_data['frame_color'] = 'lightgreen'
            self.app_data['text_color'] = 'black'
            self.app_data['artists'] = {}
        # styles
        self.style = ttk.Style()
        self.heading = font.Font(family=self.app_data['font'], size=20,
                                 weight='bold')
        self.text = font.Font(family=self.app_data['font'], size=11,
                              weight='bold')
        self.listbox_font = font.Font(family='Comic Sans MS', size=11)
        self.style.configure('TLabel', font=self.text,
                             foreground=self.app_data['text_color'], padding=5,
                             background=self.app_data['frame_color'])
        self.style.configure('TButton', font=self.text,
                             padding=5, background='blue')
        self.style.configure('TFrame', background=self.app_data['frame_color'])
        self.style.configure('TNotebook', background=self.app_data['base_color'])
        # pages
        self.p1 = ttk.Frame(self, relief='groove', padding=8)
        self.p2 = ttk.Frame(self, relief='groove', padding=8)
        self.p3 = ttk.Frame(self, relief='groove', padding=8)
        self.p4 = ttk.Frame(self, relief='groove', padding=8)
        self.p4 = ttk.Frame(self, relief='groove', padding=8)
        self.add(self.p1, text='Home', padding=2)
        self.add(self.p2, text='Current Artist', padding=2)
        self.add(self.p3, text='Current Lyrics', padding=2)
        self.add(self.p4, text='Personalization', padding=2)
        # p1 objects
        self.artists_list = StringVar()
        self.lyrics_to_search = ttk.Entry(self.p1, font=self.text)
        self.lyrics_to_search.focus()
        self.found_lyrics = ttk.Label(self.p1)
        self.found_artist = ''
        self.matched_lyrics = ''
        self.artists_listbox = Listbox(
            self.p1, listvariable=self.artists_list, font=self.listbox_font)
        self.artists_scrollbar1 = ttk.Scrollbar(
            self.p1, orient=VERTICAL, command=self.artists_listbox.yview)
        self.artists_scrollbar2 = ttk.Scrollbar(
            self.p1, orient=HORIZONTAL, command=self.artists_listbox.xview)
        self.artists_listbox['xscrollcommand'] = self.artists_scrollbar2.set
        self.artists_listbox['yscrollcommand'] = self.artists_scrollbar1.set
        self.total_artist_label = ttk.Label(self.p1)
        self.total_lyrics_label = ttk.Label(self.p1, text='0')
        self.selected_artist_label = ttk.Label(self.p1)
        self.selected_artist_total_lyrics_label = ttk.Label(self.p1)
        self.new_artist = ttk.Entry(self.p1, font=self.text)
        # p2 objects
        self.artist = ttk.Label(self.p2, font=self.heading)
        self.artist_has_lyrics = ttk.Label(self.p2)
        self.lyrics_list = StringVar()
        self.lyrics_listbox = Listbox(
            self.p2, listvariable=self.lyrics_list, font=self.listbox_font)
        self.lyrics_scrollbar1 = ttk.Scrollbar(
            self.p2, orient=VERTICAL, command=self.lyrics_listbox.yview)
        self.lyrics_scrollbar2 = ttk.Scrollbar(
            self.p2, orient=HORIZONTAL, command=self.lyrics_listbox.xview)
        self.lyrics_listbox['xscrollcommand'] = self.lyrics_scrollbar2.set
        self.lyrics_listbox['yscrollcommand'] = self.lyrics_scrollbar1.set
        self.selected_lyrics = ttk.Label(self.p2, font=self.text)
        # p3 objects
        self.lyrics = ttk.Label(self.p3, font=self.heading)
        self.lyrics_text = Text(self.p3, wrap='none')
        self.lyrics_text_scrollbar1 = ttk.Scrollbar(
            self.p3, orient=VERTICAL, command=self.lyrics_text.yview)
        self.lyrics_text_scrollbar2 = ttk.Scrollbar(
            self.p3, orient=HORIZONTAL, command=self.lyrics_text.xview)
        self.lyrics_text['xscrollcommand'] = self.lyrics_text_scrollbar2.set
        self.lyrics_text['yscrollcommand'] = self.lyrics_text_scrollbar1.set
        self.new_lyrics_name = ttk.Entry(self.p3, font=self.text)
        # p5 objects
        self.base_color = ttk.Entry(self.p4, font=self.text)
        self.frame_color = ttk.Entry(self.p4, font=self.text)
        self.text_color = ttk.Entry(self.p4, font=self.text)
        self.font = ttk.Entry(self.p4, font=self.text)
        self.base_color.insert(0, self.app_data['base_color'])
        self.frame_color.insert(0, self.app_data['frame_color'])
        self.text_color.insert(0, self.app_data['text_color'])
        self.font.insert(0, self.app_data['font'])
        # geometry management
        for i in range(16):
            self.rowconfigure(i, weight=1)
            self.p1.rowconfigure(i, weight=1)
            self.p2.rowconfigure(i, weight=1)
            self.p3.rowconfigure(i, weight=1)
            self.p4.rowconfigure(i, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
            if i not in [1, 2]:
                self.p1.columnconfigure(i, weight=1)
            if i != 4:
                self.p2.columnconfigure(i, weight=1)
                self.p3.columnconfigure(i, weight=1)
            self.p4.columnconfigure(i, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        # events
        self.root.bind('<F1>', self.show_about)
        self.root.bind('<Enter>', self.update_app)
        self.root.bind('<Key>', self.search_lyrics)
        self.artists_listbox.bind('<<ListboxSelect>>', self.show_artist_info)
        self.artists_listbox.bind('<Return>', self.visit_artist)
        self.artists_listbox.bind('<Double-1>', self.visit_artist)
        self.artists_listbox.bind('<Delete>', self.delete_artist)
        self.lyrics_listbox.bind('<<ListboxSelect>>', self.show_lyrics)
        self.lyrics_listbox.bind('<Return>', self.display_lyrics)
        self.lyrics_listbox.bind('<Double-1>', self.display_lyrics)
        self.lyrics_listbox.bind('<Delete>', self.delete_lyrics)
        self.lyrics_text.bind('<Control-s>', self.save_changes)
        self.new_artist.bind('<Return>', self.add_artist)
        self.new_lyrics_name.bind('<Return>', self.save_new_lyrics)
        self.lyrics_to_search.bind('<Return>', self.display_found_lyrics)

        self.widgets()
        self.update_app()

    def show_about(self, *args):
        window = AboutDialog(
            self, window_title='About LyricsManager',
            about_title='Lyrics Manager',
            content='Developed and written by:\n'
                    '\tDenniel Luis Saway Sadian '
                    '(https://denniel-sadian.github.io)\n\n'
                    'Date of creation:\n'
                    '\tJanuary 9, 2018\n\n'
                    'Description:\n'
                    '\tThis application lets you store, create and view '
                    'your favorite lyrics. It is written completely in '
                    'Python Programming Language and uses Tkinter as '
                    'its GUI framework.',
            image='lm.png')
        window.wm_iconbitmap('ic.ico')
        window.mainloop()
        return args

    def ask_base_color(self):
        for i in range(len(self.base_color.get())):
            self.base_color.delete(0)
        self.base_color.insert(0, askcolor()[1])

    def ask_frame_color(self):
        for i in range(len(self.frame_color.get())):
            self.frame_color.delete(0)
        self.frame_color.insert(0, askcolor()[1])

    def ask_text_color(self):
        for i in range(len(self.text_color.get())):
            self.text_color.delete(0)
        self.text_color.insert(0, askcolor()[1])

    def personalize(self):
        if self.base_color.get():
            self.style.configure('TNotebook', background=self.base_color.get())
            self.app_data['base_color'] = self.base_color.get()
        if self.frame_color.get():
            self.style.configure('TLabel', background=self.frame_color.get())
            self.style.configure('TFrame', background=self.frame_color.get())
            self.app_data['frame_color'] = self.frame_color.get()
        if self.text_color.get():
            self.style.configure('TLabel', foreground=self.text_color.get())
            self.app_data['text_color'] = self.text_color.get()
        if self.font.get():
            self.text['family'] = self.font.get()
            self.heading['family'] = self.font.get()
            self.app_data['font'] = self.font.get()

    def update_app(self, *args):
        self.total_artist_label['text'] = len(self.app_data['artists'])
        self.artists_list.set(list(self.app_data['artists'].keys()))
        for i in range(0, len(list(self.app_data['artists'].keys())), 2):
            self.artists_listbox.itemconfigure(i, background='#f0f0ff')
        if self.artist['text']:
            self.selected_artist_total_lyrics_label['text'] = \
                len(self.app_data['artists']
                    [self.selected_artist_label['text']])
            self.artist_has_lyrics['text'] = \
                f'Has {self.selected_artist_total_lyrics_label["text"]} ' \
                'lyric(s)'
            self.lyrics_list.set(list(self.app_data['artists'][self.artist[
                'text']].keys()))
            for i in range(0, len(list(self.app_data['artists'][
                                           self.artist['text']].keys())), 2):
                self.lyrics_listbox.itemconfigure(i, background='#f0f0ff')
        self.total_lyrics_label['text'] = '0'
        for artist in list(self.app_data['artists'].keys()):
            self.total_lyrics_label['text'] = int(
                self.total_lyrics_label['text']
            ) + len(self.app_data['artists'][artist])
        return args

    def add_artist(self, *args):
        if self.new_artist.get():
            if self.new_artist.get() not in \
                    list(self.app_data['artists'].keys()):
                temporary = self.app_data['artists']
                temporary[self.new_artist.get()] = {}
                self.app_data['artists'] = temporary
                for i in range(len(self.new_artist.get())):
                    self.new_artist.delete(0)
            else:
                messagebox.showinfo('Info', f"{self.new_artist.get()} is "
                                            "already present.")
        self.update_app()
        return args

    def visit_artist(self, *args):
        if self.selected_artist_label['text']:
            self.select(1)
            self.artist['text'] = self.selected_artist_label['text']
            self.artist_has_lyrics['text'] = \
                f'Has {self.selected_artist_total_lyrics_label["text"]} lyric/s'
            self.lyrics_list.set(list(
                self.app_data['artists'][self.artist['text']].keys()))
            self.lyrics_text.delete('1.0', END)
            self.lyrics['text'] = ''
            self.lyrics_listbox.focus()
        return args

    def delete_artist(self, *args):
        if self.selected_artist_label['text'] and \
                messagebox.askokcancel(
                    'Delete', f"{self.selected_artist_label['text']} will be "
                              "deleted from the app's database and all "
                              "the lyrics he/she contains."):
            temporary = self.app_data['artists']
            del temporary[self.selected_artist_label['text']]
            self.app_data['artists'] = temporary
            self.selected_artist_label['text'] = ''
            self.selected_artist_total_lyrics_label['text'] = ''
            self.artist['text'] = ''
            self.selected_lyrics['text'] = ''
            self.lyrics['text'] = ''
        self.update_app()
        return args

    def show_artist_info(self, *args):
        if len(self.artists_listbox.curselection()) == 1:
            self.selected_artist_label['text'] = list(
                self.app_data['artists'].keys())[int(
                    self.artists_listbox.curselection()[0])]
            self.selected_artist_total_lyrics_label['text'] = len(
                self.app_data['artists'][self.selected_artist_label['text']])
        return args

    def show_lyrics(self, *args):
        if len(self.lyrics_listbox.curselection()) == 1:
            self.selected_lyrics['text'] = list(
                self.app_data['artists'][self.artist['text']].keys())[int(
                    self.lyrics_listbox.curselection()[0])]
        return args

    def display_lyrics(self, *args):
        if self.selected_lyrics['text']:
            self.select(2)
            self.lyrics['text'] = self.selected_lyrics['text']
            self.lyrics_text.delete('1.0', 'end')
            self.lyrics_text.insert(
                '1.0', self.app_data['artists'][self.artist['text']][
                    self.lyrics['text']])
            self.lyrics_text.focus()
        return args

    def delete_lyrics(self, *args):
        if self.selected_lyrics['text'] and \
                messagebox.askokcancel(
                    'Delete', f"{self.selected_lyrics['text']} will be deleted"):
            temporary = self.app_data['artists']
            del temporary[self.artist['text']][self.selected_lyrics['text']]
            self.app_data['artists'] = temporary
            self.selected_lyrics['text'] = ''
        self.update_app()
        return args

    def save_new_lyrics(self, *args):
        if self.new_lyrics_name.get() and self.lyrics_text.get('1.0', 'end') \
                and self.artist['text']:
            if self.new_lyrics_name.get() not in \
                    list(self.app_data['artists'][self.artist['text']].keys()):
                artist = self.app_data['artists']
                artist[self.artist['text']][self.new_lyrics_name.get()] = \
                    self.lyrics_text.get('1.0', 'end').strip()
                self.app_data['artists'] = artist
                self.lyrics['text'] = self.new_lyrics_name.get()
                messagebox.showinfo('Info', f"{self.new_lyrics_name.get()} has "
                                            f"been saved to the database.")
                for i in range(len(self.new_lyrics_name.get())):
                    self.new_lyrics_name.delete(0)
            else:
                messagebox.showinfo('Info', f"{self.new_lyrics_name.get()} is "
                                            "already present.")
        self.update_app()
        return args

    def save_changes(self, *args):
        if self.lyrics['text'] and self.lyrics_text.get('1.0', 'end'):
            artist = self.app_data['artists']
            artist[self.artist['text']][self.lyrics['text']] = \
                self.lyrics_text.get('1.0', 'end').strip()
            self.app_data['artists'] = artist
            messagebox.showinfo('Info', 'Saved')
        self.update_app()
        return args

    def display_found_lyrics(self, *args):
        if self.found_artist and self.matched_lyrics:
            self.selected_artist_label['text'] = self.found_artist
            self.selected_lyrics['text'] = self.matched_lyrics
            self.visit_artist()
            self.display_lyrics()
            self.found_lyrics['text'] = ''
            self.found_artist = ''
            self.matched_lyrics = ''
            for i in range(len(self.lyrics_to_search.get())):
                self.lyrics_to_search.delete(0)
        return args

    def search_lyrics(self, *args):
        should_break = False
        if self.lyrics_to_search.get():
            for artist in list(self.app_data['artists'].keys()):
                if should_break:
                    break
                for lyrics in list(self.app_data['artists'][artist].keys()):
                    if self.lyrics_to_search.get().lower() in lyrics.lower():
                        self.found_lyrics['text'] = f'{artist} - {lyrics}'
                        self.found_artist = artist
                        self.matched_lyrics = lyrics
                        should_break = True
                        break
                    else:
                        self.found_lyrics['text'] = 'Lyrics not found'
                        self.found_artist = ''
                        self.matched_lyrics = ''
        else:
            self.found_lyrics['text'] = ''
            self.found_artist = ''
            self.matched_lyrics = ''
        return args

    def widgets(self):
        # p1
        ttk.Label(self.p1, text='Lyrics Manager', font=self.heading).grid(
            column=0, row=0, columnspan=5)
        ttk.Label(self.p1, text='Where you can find your lyrics in one'
                                ' place').grid(
            column=0, row=1, columnspan=5)
        ttk.Separator(self.p1, orient=HORIZONTAL).grid(
            column=0, row=2, columnspan=5, sticky='WE', pady=10)
        ttk.Separator(self.p1, orient=VERTICAL).grid(
            column=2, row=3, rowspan=13, sticky='NS', padx=10)
        ttk.Label(self.p1, text='Search Lyrics').grid(
            column=0, row=3, columnspan=2)
        self.lyrics_to_search.grid(column=0, row=4, columnspan=2, sticky='WE')
        self.found_lyrics.grid(column=0, row=5, columnspan=2)
        ttk.Button(self.p1, text='Display found Lyrics',
                   command=self.display_found_lyrics).grid(
            column=0, row=6, sticky='WE', columnspan=2)
        ttk.Separator(self.p1, orient=HORIZONTAL).grid(
            column=0, row=7, sticky='WE', columnspan=2, pady=5)
        self.artists_listbox.grid(column=0, row=8, sticky='NEWS', rowspan=7)
        self.artists_scrollbar1.grid(column=1, row=8, sticky='NWS', rowspan=7)
        self.artists_scrollbar2.grid(column=0, row=15, sticky='WNE')
        ttk.Label(self.p1, text='Total Artists:').grid(column=3, row=3)
        self.total_artist_label.grid(column=4, row=3)
        ttk.Label(self.p1, text='Total Lyrics:').grid(column=3, row=4)
        self.total_lyrics_label.grid(column=4, row=4)
        ttk.Separator(self.p1, orient=HORIZONTAL).grid(
            column=3, row=5, columnspan=2, sticky='WE', pady='5 10')
        ttk.Label(self.p1, text='Selected Artist:').grid(column=3, row=6)
        self.selected_artist_label.grid(column=4, row=6)
        ttk.Label(self.p1, text='Lyrics:').grid(column=3, row=7)
        self.selected_artist_total_lyrics_label.grid(column=4, row=7)
        ttk.Button(self.p1, text='Visit Artist', command=self.visit_artist).grid(
            column=3, row=8, columnspan=2, sticky='WE')
        ttk.Button(self.p1, text='Delete Artist',
                   command=self.delete_artist).grid(
            column=3, row=9, sticky='WE', columnspan=2)
        ttk.Separator(self.p1, orient=HORIZONTAL).grid(
            column=3, row=10, columnspan=2, sticky='WE', pady='5 10')
        ttk.Label(self.p1, text='Add New Artist').grid(
            column=3, row=11, columnspan=2)
        self.new_artist.grid(column=3, row=12, sticky='WE', columnspan=2)
        ttk.Button(self.p1, text='Add Artist', command=self.add_artist).grid(
            column=3, row=13, columnspan=2, sticky='WE')
        # p2
        self.artist.grid(column=0, row=0, columnspan=5)
        self.artist_has_lyrics.grid(column=0, row=1, columnspan=5)
        ttk.Separator(self.p2, orient=HORIZONTAL).grid(
            column=0, row=2, sticky='WE', columnspan=5, pady='0 10')
        self.lyrics_listbox.grid(
            column=0, row=3, sticky='NEWS', columnspan=4, rowspan=6)
        self.lyrics_scrollbar1.grid(column=4, row=3, rowspan=6, sticky='NWS')
        self.lyrics_scrollbar2.grid(column=0, row=9, columnspan=4, sticky='WEN')
        ttk.Separator(self.p2, orient=HORIZONTAL).grid(
            column=0, row=10, sticky='WE', columnspan=5, pady='5 10')
        ttk.Label(self.p2, text='Selected Lyrics:').grid(
            column=0, row=11, columnspan=5)
        self.selected_lyrics.grid(column=0, row=12, columnspan=5)
        ttk.Separator(self.p2, orient=HORIZONTAL).grid(
            column=0, row=13, sticky='WE', columnspan=5, pady='5 10')
        ttk.Button(self.p2, text='Display', command=self.display_lyrics).grid(
            column=0, row=14, sticky='WE', columnspan=5)
        ttk.Button(self.p2, text='Delete', command=self.delete_lyrics).grid(
            column=0, row=15, sticky='WE', columnspan=5)
        # p3
        self.lyrics.grid(column=0, row=0, columnspan=5)
        ttk.Separator(self.p3, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5, pady='5 10')
        self.lyrics_text.grid(
            column=0, row=2, columnspan=4, rowspan=10, sticky='NEWS')
        self.lyrics_text_scrollbar1.grid(column=4, row=2, rowspan=10,
                                         sticky='WNS')
        self.lyrics_text_scrollbar2.grid(column=0, row=12, columnspan=4,
                                         sticky='WEN')
        ttk.Separator(self.p3, orient=HORIZONTAL).grid(
            column=0, row=13, sticky='WE', columnspan=5, pady=10)
        ttk.Button(self.p3, text='Save Changes', command=self.save_changes).grid(
            column=0, row=14, columnspan=5, sticky='WE', pady='0 10')
        self.new_lyrics_name.grid(column=0, row=15, sticky='NEWS', columnspan=3)
        ttk.Button(self.p3, text='Save new lyrics',
                   command=self.save_new_lyrics).grid(
            column=3, row=15, columnspan=2, sticky='WE', padx='3 0')
        # p5
        ttk.Label(self.p4, text='Personalization', font=self.heading).grid(
            column=0, row=0, columnspan=5)
        ttk.Label(self.p4, text="You can change the app's appearance here").grid(
            column=0, row=1, columnspan=5)
        ttk.Separator(self.p4, orient=HORIZONTAL).grid(
            column=0, row=2, sticky='WE', columnspan=5, pady=10)
        ttk.Label(self.p4, text='Base color:').grid(column=0, row=3)
        ttk.Label(self.p4, text='Frame color:').grid(column=0, row=4)
        ttk.Label(self.p4, text='Text color:').grid(column=0, row=5)
        ttk.Label(self.p4, text='Font:').grid(column=0, row=6)
        self.base_color.grid(column=1, row=3, columnspan=2, sticky='WE')
        ttk.Button(self.p4, text='Choose base color',
                   command=self.ask_base_color).grid(
            column=3, row=3, columnspan=2, sticky='WE', padx='3 0')
        self.frame_color.grid(column=1, row=4, columnspan=2, sticky='WE')
        ttk.Button(self.p4, text='Choose frame color',
                   command=self.ask_frame_color).grid(
            column=3, row=4, columnspan=2, sticky='WE', padx='3 0')
        self.text_color.grid(column=1, row=5, columnspan=2, sticky='WE')
        ttk.Button(self.p4, text='Choose frame color',
                   command=self.ask_text_color).grid(
            column=3, row=5, columnspan=2, sticky='WE', padx='3 0')
        self.font.grid(column=1, row=6, columnspan=4, sticky='WE')
        ttk.Separator(self.p4, orient=HORIZONTAL).grid(
            column=0, row=7, sticky='WE', columnspan=5, pady=10)
        ttk.Button(self.p4, text='Save', command=self.personalize).grid(
            column=0, row=8, sticky='WE', columnspan=5)


if __name__ == '__main__':
    root = Tk()
    app = LyricsManager(root, padding='3 5 3 3')
    app.grid(column=0, row=0, sticky='NEWS')
    root.title('Lyrics Manager App')
    root.wm_iconbitmap('ic.ico')
    root.geometry('600x650+5+10')
    root.mainloop()
