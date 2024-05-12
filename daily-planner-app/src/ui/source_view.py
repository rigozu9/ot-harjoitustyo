"""importing tkinter and webbrowser"""
import tkinter as tk
import webbrowser

class SourcePageView:
    #generöity koodi alkaa
    """View for displaying categorized advice links in the application."""
    def __init__(self, master, user_id, views):
        self._master = master
        self._user_id = user_id
        self._handle_show_advice_view = views['user_advice']

        # Create a scrollable frame to hold the content
        self._scroll_canvas = tk.Canvas(self._master)
        self._scroll_frame = tk.Frame(self._scroll_canvas)
        self._scrollbar = tk.Scrollbar(self._master, orient="vertical",
                                       command=self._scroll_canvas.yview)
        self._scroll_canvas.configure(yscrollcommand=self._scrollbar.set)
        self._scrollbar.pack(side="right", fill="y")
        self._scroll_canvas.pack(side="left", fill="both", expand=True)
        self._scroll_canvas.create_window((0, 0), window=self._scroll_frame, anchor="nw")
        self._scroll_frame.bind("<Configure>", self._on_frame_configure)

        self._add_links()

        self._goto_advice_page_button = tk.Button(
            self._scroll_frame, text="Go to advice page",
            command=self._goto_advice_view)
        self._goto_advice_page_button.pack()

    def _on_frame_configure(self):
        """Reset the scroll region to encompass the inner frame"""
        self._scroll_canvas.configure(scrollregion=self._scroll_canvas.bbox("all"))

    def _add_links(self):
        """Add links to the frame"""
        links = {
            'Sleep': [
                "https://www.sleepfoundation.org/how-sleep-works/how-much-sleep-do-we-really-need",
                "https://www.nhlbi.nih.gov/health/sleep-deprivation/health-effects",
                "https://www.cdc.gov/sleep/about_sleep/sleep_hygiene.html"
            ],
            'Exercise': [
                "https://www.cdc.gov/physicalactivity/basics/adults/index.htm",
                "https://health.clevelandclinic.org/benefits-of-exercise-other-than-weight-loss",
                "https://www.healthdirect.gov.au/exercise-and-mental-health"
            ],
            'Outside time': [
                "https://www.menshealth.com/fitness/a36547849/how-much-time-" +
                "should-i-spend-outside/",
                "https://www.hsph.harvard.edu/news/hsph-in-the-news/spend-time-outdoors-"+
                "itll-improve-your-health-say-experts/",
                "https://www.healthline.com/health/health-benefits-of-being-outdoors"
            ],
            'Productive': [
                "https://www.atlassian.com/blog/productivity/this-is-how-" +
                "many-hours-you-should-really-be-working",
                "https://habitgrowth.com/advantages-of-being-productive/",
                "https://www.verywellmind.com/how-to-be-more-productive-6499714"
            ],
            'Screentime': [
                "https://www.reidhealth.org/blog/screen-time-for-adults",
                "https://www.mayoclinichealthsystem.org/hometown-health/featured-topic/" +
                "5-ways-slimming-screen-time-is-good-for-your-health",
                "https://www.heart.org/en/news/2024/02/29/tips-for-reducing-screen" +
                "-time-and-why-that-might-be-a-good-idea"
            ]
        }

        for category, urls in links.items():
            label = tk.Label(self._scroll_frame, text=category, font=('Arial', 16, 'bold'))
            label.pack(pady=10)
            for url in urls:
                link = tk.Label(self._scroll_frame, text=url, font=('Arial', 10), 
                                fg="blue", cursor="hand2")
                link.pack()
                link.bind("<Button-1>", lambda e, url=url: webbrowser.open_new(url))

        #generöity koodi loppuu
    def _goto_advice_view(self):
        """going to advice page button."""
        self._scroll_canvas.destroy()
        self._scroll_frame.destroy()
        self._scrollbar.destroy()
        self._handle_show_advice_view(self._user_id)
