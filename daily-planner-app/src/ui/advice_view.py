"""importing tkinter, datetime and messagebox"""
import tkinter as tk
import webbrowser
import re
import random

class AdvicePageView:
    """Daily planner view for the application"""

    def __init__(self, master, user_id, user_service, daily_plan_service, views):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)

        self._handle_show_user_info_view = views['user_info']
        self._handle_show_source_view = views['source']


        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"Tailored daily habit improvements for {self._username}",
            font=('Arial', 18))
        self._welcome_label.pack()

        self._goals_label = tk.Label(
            self._frame, text="Based on your goals:",
            font=('Arial', 13))
        self._goals_label.pack()

        self._show_goals_improvements()

        self._welcome_label = tk.Label(
            self._frame, text="Based on your averages:",
            font=('Arial', 13))
        self._welcome_label.pack()

        self._show_average_improvements()

        self._info_button = tk.Button(
            self._frame, text="Your profile", command=self._go_to_userpage)
        self._info_button.pack()

        self._info_button = tk.Button(
            self._frame, text="Sources", command=self._go_to_sources)
        self._info_button.pack()

        self._frame.pack()

    def _create_and_pack_label(self, text, frame):
        """
            Helper function to create a label with the 
            specified text and pack it into the given frame.
        """
        label = tk.Label(frame, text=text, wraplength=500, justify='left', anchor='w', padx=10)
        label.pack(fill='x', padx=20, pady=5)

    #koodin generöinti alkaa
    def _create_and_pack_text(self, text, frame):
        """
        Helper function to create a text widget with optional hyperlinks and
        pack it into the given frame. Randomly selects one hyperlink to display.
        """
        text_widget = tk.Text(frame, height=2, wrap='word', cursor="arrow",
                            padx=10, pady=5, font=('Arial', 10), bg='lightgrey')
        url_pattern = r'(https?://\S+)'  # Regex pattern to find URLs
        urls = []  # List to store found URLs with their positions

        start = 0
        for match in re.finditer(url_pattern, text):
            url = match.group(0)
            urls.append((url, match.start(), match.end()))  # Store URL and positions
            text_widget.insert('end', text[start:match.start()])  # Insert text up to the URL
            start = match.end()  # Update start to end of the current URL

        # Insert any remaining text after the last URL if no URLs found
        if not urls:
            text_widget.insert('end', text)
        else:
            selected_url, start_pos, end_pos = random.choice(urls)  # Randomly select one URL
            # Insert the selected URL with hyperlink
            text_widget.insert('end', text[start_pos:end_pos], 'hyper')
            text_widget.tag_bind('hyper', "<Enter>",
                                lambda e, url=selected_url: text_widget.config(cursor="hand2"))
            text_widget.tag_bind('hyper', "<Leave>",
                                lambda e, url=selected_url: text_widget.config(cursor="arrow"))
            text_widget.tag_bind('hyper', "<Button-1>",
                                lambda e, url=selected_url: webbrowser.open_new(url))
            # Insert any text after the selected URL
            text_widget.insert('end', text[end_pos:])

        text_widget.tag_configure("hyper", foreground="blue", underline=1)
        text_widget.config(state='disabled')
        text_widget.pack(fill='x', padx=20, pady=5)
    #koodin generöinti loppuu


    def _show_goals_improvements(self):
        goals = self._user_service.show_info(self._user_id)
        goal_advice_dict = self._user_service.get_advice(goals)[0]
        for _, advice_text in goal_advice_dict.items():
            self._create_and_pack_text(advice_text, self._frame)

    def _show_average_improvements(self):
        averages = self._daily_plan_service.calculate_average_attributes(self._user_id)
        average_advice_dict = self._user_service.get_advice(None, averages)[1]
        for _, advice_text in average_advice_dict.items():
            self._create_and_pack_text(advice_text, self._frame)

    def _go_to_userpage(self):
        """go to userinfoview"""
        self._frame.destroy()
        self._handle_show_user_info_view(self._user_id)

    def _go_to_sources(self):
        """go to sourcepage"""
        self._frame.destroy()
        self._handle_show_source_view(self._user_id)