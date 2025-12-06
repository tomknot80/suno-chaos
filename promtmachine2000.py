import random
import tkinter as tk
from tkinter import messagebox, filedialog, Canvas, Scrollbar

class PromptMakerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Prompt Maker with Lyrics")
        self.root.geometry("1000x900")

        # Expanded prompt element lists
        self.themes = [
            "Acid Rock", "Alternative Rock", "Art Rock", "Atmospheric Black Metal", "Avant-garde Metal",
            "Black Metal", "Blues Rock", "Classic Rock", "Comedy Rock", "Country Rock", "Death Metal",
            "Deathcore", "Desert Rock", "Doom Metal", "Electronic Rock", "Experimental Metal",
            "Experimental Rock", "Folk Metal", "Folk Rock", "Funk Metal", "Funk Rock", "Garage Rock",
            "Glam Rock", "Gothic Metal", "Gothic Rock", "Groove Metal", "Grunge", "Hard Rock",
            "Heavy Metal", "Heavy Metal Trap", "Industrial Metal", "Industrial Rock", "Instrumental Rock",
            "Kawaii Metal", "Math Rock", "Melodic Death Metal", "Melodic Metalcore", "Metal",
            "Metalcore", "New York Hardcore", "Noise Rock", "Nu Metal", "Oriental Metal", "Pagan Metal",
            "Piano Rock", "Post-Metal", "Post-Rock", "Power Metal", "Progressive Metal",
            "Progressive Rock", "Psychedelic Rock", "Punk Rock", "Rap Metal", "Rap Rock", "Rock",
            "Rock and Roll", "Rock Opera", "Rockabilly", "Scandinavian Metal", "Skate Rock",
            "Sludge Metal", "Southern Rock", "Space Rock", "Speed Metal", "Stadium Rock", "Stoner Rock",
            "Surf Rock", "Symphonic Black Metal", "Symphonic Metal", "Symphonic Rock", "Thrash Metal",
            "Viking Metal", "War Metal", "Acid Jazz", "Ambient", "Bass House", "Brostep", "Chillwave",
            "Club", "Cyberpunk", "Dance", "Dance Pop", "Dark Ambient", "Dark Electro", "Deep House",
            "Deep Techno", "Downtempo", "Drone", "Dub", "Dub Techno", "Dubstep", "EDM", "Electro",
            "Electro Swing", "Electroacoustic", "Electronic", "Electropop", "Eurodance", "French House",
            "Future Bass", "Future Garage", "Future House", "Gabber", "Glitch", "Glitch Hop",
            "Glitch Pop", "Goa Trance", "Happy Hardcore", "Hardstyle", "House", "Hyperpop",
            "IDM (Intelligent Dance Music)", "Industrial", "Jungle", "Minimal Techno", "Moombahton",
            "Neurofunk", "Nu Disco", "Post-Disco", "Post-Dubstep", "Progressive House", "Psybient",
            "Psychedelic Trance", "Rave", "Space Disco", "Synthwave", "Tech House", "Techno",
            "Trance", "Trip Hop", "Tropical House", "UK Funky", "UK Garage", "Vaporwave",
            "Vocal House", "Vocal Trance", "Witch House", "Bebop", "Big Band", "Blues", "Cool Jazz",
            "Dark Jazz", "Delta Blues", "Gypsy Jazz", "Hard Bop", "Jazz", "Jazz Fusion", "Jazz Rap",
            "Latin Jazz", "Modal Jazz", "New Orleans Jazz", "Nu Jazz", "Piano Blues", "Piedmont Blues",
            "Post-Bop", "Punk Blues", "Smooth Jazz", "Soul Jazz", "Swing", "Crunk", "Hip Hop",
            "Mumble Rap", "Pop Rap", "Rap", "Trap", "UK Drill", "West Coast Rap", "Afro-Cuban",
            "Afrobeat", "Arabian", "Arabian Ornamental", "Bangra", "Bluegrass", "Bolero", "Calypso",
            "Carnatic", "Celtic", "Chalga", "Chanson", "Country", "Country Blues", "Fado", "Flamenco",
            "Folk", "Folk Punk", "Forró", "Freak Folk", "Guajira", "Hawaiian", "Hindustani",
            "Honky Tonk", "Indian Classical", "Indie Folk", "Irish Folk", "Klezmer", "Latin",
            "Mambo", "Mariachi", "Neofolk", "Nordic Folk", "Outlaw Country", "Polka", "Qawwali",
            "Quebecois Traditional", "Rai", "Ranchera", "Reggae", "Reggaeton", "Roots Reggae",
            "Rumba", "Russian Folk", "Salsa", "Samba", "Sea Shanties", "Sephardic", "Spanish Folk",
            "Sufi Music", "Taarab", "Tango", "Traditional", "Traditional Folk", "Tribal",
            "Truck Driving Country", "Urban Folk", "World", "World Beat", "World Fusion", "Zydeco",
            "Adult Contemporary", "Bedroom", "Broadway", "Disco", "Disco Funk", "Dream Pop", "Emo",
            "Europop", "Funk", "Indie", "Indie Pop", "Indie Rock", "J-pop", "K-pop", "Latin Pop",
            "Lounge", "Motown", "Neon Pop", "Noise Pop", "Pop", "Pop Punk", "Pop Rock", "Power Pop",
            "Psychedelic Pop", "R&B", "Contemporary R&B", "Singer-Songwriter", "Soft Rock", "Soul",
            "Synth-pop", "Thai Pop", "Urban Contemporary", "Avant-garde Jazz", "Dark Cabaret",
            "Dungeon Synth", "Experimental", "Harsh Noise", "Martial Industrial", "Musique Concrète",
            "Noise", "No Wave", "Power Electronics", "Sound Art", "Sound Collage", "Tape Music",
            "Adagio", "Allegro", "Andante", "Chamber Music", "Classical Crossover",
            "Contemporary Classical", "Modern Classical", "Neoclassical", "Opera", "Operatic Pop",
            "Orchestral", "Organum", "Partita", "Requiem", "Rhapsody", "Romantic", "Schoenberg",
            "Serialism", "Sonata", "Spectralism", "String Quartet", "Symphonic", "Symphony",
            "Twelve-tone", "Acapella", "Barbershop", "Beatboxing", "Choir", "Christmas Carol",
            "Doo Wop", "Gregorian Chant", "Islamic Call to Prayer", "Throat Singing", "Vocal",
            "Vocal Jazz", "Vocaloid", "Audiobook Background", "Background", "Cinematic",
            "Movie Soundtrack", "Score", "Spaghetti Western", "TV Themes", "Video Game Music",
            "Villain Theme",
            "Afrofuturism", "Balkan Brass", "Baroque Pop", "Bossa Nova", "Breakcore", "Bubblegum Pop",
            "C86", "Candombe", "Chiptune", "Cloud Rap", "Cumbia Rebajada", "Cybergrind",
            "Darkwave", "Digital Hardcore", "Drill", "Drone Metal", "East Coast Hip Hop",
            "Electroclash", "Emo Rap", "Enka", "Ethereal Wave", "Footwork", "Freestyle",
            "Future Funk", "Gamelan", "Ghettotech", "Grime", "Highlife", "Horrorcore",
            "Italo Disco", "Jangle Pop", "Juju", "Krautrock", "Lo-Fi Hip Hop", "Madchester",
            "Makossa", "Mathcore", "Microhouse", "Morna", "New Wave", "Nightcore",
            "Norteño", "Pirate Metal", "Post-Punk", "Ragtime", "Shoegaze", "Ska Punk",
            "Soca", "Sophisti-Pop", "Soukous", "Surf Punk", "Tejano", "Zouk"
        ]

        self.moods = [
            "Aggressive", "Anthemic", "Atmospheric", "Calming", "Chaotic", "Dark", "Emotional",
            "Epic", "Ethereal", "Festive", "Groovy", "Haunted", "Intimate", "Melancholy",
            "Minimal", "Narrative", "Nostalgic", "Party", "Sensitive", "Uplifting", "Vintage",
            "Doom", "Mystery", "Tension", "Awe", "Chaos", "Melancholic", "Triumph", "Dread",
            "Serenity", "Frenzy", "Hope", "Despair", "Euphoria", "Unease", "Rage", "Suspense",
            "Bliss", "Grief", "Madness", "Calm", "Urgency", "Whimsy", "Sorrow", "Excitement",
            "Fear", "Joy", "Bitterness", "Longing", "Pride", "Shame", "Wonder", "Panic",
            "Peace", "Aggression", "Solitude", "Yearning", "Defiance", "Resignation", "Intrigue",
            "Devotion", "Hysteria", "Reverence", "Anguish", "Glee", "Apathy", "Confusion",
            "Clarity", "Obsession", "Relief", "Sultry", "Playful", "Haunting", "Mysterious",
            "Hypnotic", "Dreamy", "Confident", "Desperate", "Tranquil", "Emotive", "Angsty",
            "Triumphant", "Introspective", "Detached",
            "Alienated", "Buoyant", "Cathartic", "Chilled", "Cinematic", "Contemplative",
            "Cosmic", "Cryptic", "Defiant", "Disorienting", "Ecstatic", "Enigmatic",
            "Exhilarating", "Feverish", "Foreboding", "Giddy", "Gritty", "Heartfelt",
            "Icy", "Languid", "Luminous", "Menacing", "Optimistic", "Pensive",
            "Quirky", "Radiant", "Restless", "Sardonic", "Somber", "Thrilling",
            "Unsettling", "Vibrant", "Wistful"
        ]

        self.instruments = [
            "violin concerto", "string orchestra", "brass fanfare", "sub-bass", "choir", "pipe organ",
            "harpsichord", "electric guitar", "synthesizer", "drums", "flute", "cello solo", "piano",
            "trumpet ensemble", "harp", "duduk", "theremin", "accordion", "sitar", "taiko drums",
            "bagpipes", "music box", "soundscape drones", "chimes", "oboe", "clarinet", "saxophone",
            "bassoon", "french horn", "trombone", "tuba", "mandolin", "banjo", "ukulele", "lute",
            "balalaika", "koto", "shamisen", "erhu", "didgeridoo", "marimba", "xylophone",
            "steel drums", "handpan", "tabla", "bongos", "congas", "djembes", "glass harmonica",
            "kalimba", "acoustic guitar", "bass guitar", "turntables", "rapping", "yodeling",
            "scatting", "beatboxing", "vocal ensemble",
            "berimbau", "bodhrán", "bouzouki", "charango", "guzheng", "hurdy-gurdy",
            "jaw harp", "kora", "mbira", "ney", "oud", "pan flute", "rebab",
            "santoor", "shakuhachi", "shehnai", "sousaphone", "talking drum",
            "tres", "veena", "vibraphone", "whistling", "vocal percussion"
        ]

        self.effects = [
            "demonic vibrato", "infernal tremolo", "microtonal glissando", "reverb", "pitch shift",
            "distortion", "echo", "delay", "phaser", "flanger", "reverse", "overdrive", "chorus",
            "stutter", "granular synthesis", "bitcrush", "wah-wah", "arpeggio", "tape loop",
            "white noise", "pulsating drone", "metallic clang", "whisper overlay", "spectral warp",
            "harmonic resonance", "feedback loop", "low-pass filter", "high-pass filter",
            "band-pass filter", "ring modulation", "vocoder", "autotune", "sidechain compression",
            "gated reverb", "shimmer", "detune", "sweep", "pulse width modulation", "crackle",
            "hum", "doppler shift", "phase cancellation", "flutter", "warble", "sizzle",
            "drone swell", "pitch bend", "time stretch", "formant shift", "auto-tuned",
            "layered", "chopped", "filtered", "robotized", "phased", "flanged", "lo-fi",
            "bit-crushed", "glitched", "stuttered", "modulated", "panned left", "panned right",
            "granular", "doubled", "auto-harmonized", "saturated", "ring-modulated", "detuned",
            "reverbed", "echoed", "staccato", "legato", "vibrato-heavy", "monotone", "melismatic",
            "syncopated", "operatic", "chanting", "spoken-word", "growling", "belting", "humming",
            "falsetto runs", "yelping", "grunting", "call-and-response", "soft-spoken", "shouted",
            "crescendo", "decrescendo", "sudden stop", "building intensity", "explosive", "subtle",
            "whispered vocals", "breathy build-up", "intense climax", "dynamic shifts",
            "fading vocals", "echoing softly", "reverb swell", "silent break", "airy", "breathy",
            "crisp", "deep", "gritty", "smooth", "soft", "warm", "raw", "sharp", "muffled",
            "bright", "mellow", "raspy", "clear", "thin", "dense", "whispered", "gravelly",
            "velvety", "dreamy", "resonant", "nasal", "brassy", "metallic", "smoky", "chilled",
            "rough-edged", "shimmery", "glassy", "crunchy", "liquid-like", "breathy exhale",
            "ambient wash", "binaural beats", "crossfade", "de-essing", "dynamic EQ",
            "field recording", "frequency modulation", "harmonic distortion", "isolation",
            "mid-side processing", "multiband compression", "parallel processing",
            "pitch correction", "reverse reverb", "saturation", "spatial widening",
            "stereo imaging", "tape saturation", "transient shaping", "vinyl crackle",
            "vocal layering", "vocal morphing", "vocal tuning", "warm distortion",
            "clicks and pops", "digital glitch", "lo-fi tape hiss", "synthetic chirp",
            "textured noise", "underwater effect"
        ]

        self.settings = [
            "cathedral of bones", "abyssal rift", "shattered realm", "eternal storm", "void temple",
            "haunted forest", "crumbling castle", "frozen tundra", "deserted city", "orbital station",
            "underground cavern", "ghost ship", "crystal palace", "swamp of despair", "mountain peak",
            "clockwork factory", "astral plane", "forgotten battlefield", "labyrinthine ruins",
            "submerged cathedral", "neon-lit streets", "volcanic wasteland", "ethereal garden",
            "cosmic vortex", "ancient library", "floating islands", "dark ocean depths",
            "burning desert", "twisted jungle", "ruined coliseum", "silent monastery",
            "glowing wasteland", "phantom city", "sky fortress", "hidden oasis", "cursed village",
            "radiant plateau", "shadowed valley", "mechanical abyss", "spectral plains",
            "glacial fortress", "mirrored lake", "infernal forge", "starlit dunes", "toxic marsh",
            "sunken citadel", "celestial observatory", "warped dimension", "timeless desert",
            "post-apocalyptic skyline", "cybernetic jungle", "haunted carnival", "alien ruins",
            "abandoned arcade", "arctic mirage", "bamboo grove", "cosmic bazaar",
            "crimson canyon", "dystopian slums", "enchanted coral reef", "foggy moor",
            "futuristic dojo", "geothermal springs", "haunted opera house", "lunar colony",
            "moss-covered ruins", "neon jungle", "pirate cove", "retro diner",
            "steampunk airship", "sunken pirate ship", "tropical lagoon", "underground speakeasy",
            "wind-swept prairie"
        ]

        self.time_periods = [
            "Medieval", "Renaissance", "Baroque", "Victorian", "Roaring 20s", "1950s",
            "1960s", "1970s", "1980s", "1990s", "Early 2000s", "Futuristic",
            "Cyberpunk 2077", "Steampunk 1890s", "Post-Apocalyptic 2200", "Ancient Mesopotamia",
            "Feudal Japan", "Colonial Era", "Space Age 1960s", "Near-Future 2030",
            "Distant Future 3000"
        ]

        self.cultural_influences = [
            "Andalusian", "Balinese", "Berber", "Brazilian", "Cajun", "Caribbean",
            "Chinese", "Egyptian", "Ethiopian", "Greek", "Inuit", "Japanese",
            "Maori", "Mongolian", "Persian", "Polynesian", "Roma", "Sami",
            "South Indian", "Tibetan", "West African"
        ]

        self.narrative_themes = [
            "hero’s journey", "forbidden love", "cosmic exploration", "revenge saga",
            "ghostly encounter", "dystopian rebellion", "mythical quest", "time travel",
            "apocalyptic survival", "pirate adventure", "alien invasion", "haunted past",
            "rags to riches", "betrayal and redemption", "war and peace", "nature’s wrath",
            "technological singularity", "dream within a dream", "prophecy fulfilled",
            "exile and return"
        ]

        self.lyrical_themes = [
            "love and heartbreak", "rebellion and freedom", "nature and wilderness", "cosmic journey",
            "urban life", "spiritual awakening", "war and peace", "nostalgia and memory",
            "hope and resilience", "loss and grief", "adventure and exploration", "identity and self-discovery",
            "myth and legend", "technology and dystopia", "celebration and joy", "struggle and survival",
            "dreams and surrealism", "betrayal and revenge", "friendship and loyalty", "mystery and intrigue"
        ]

        self.vocal_styles = [
            "soprano", "alto", "tenor", "bass", "rap", "crooning", "falsetto", "growling",
            "operatic", "spoken word", "harmonized", "scatting", "yodeling", "chanting",
            "melodic shouting", "breathy", "grunge scream", "smooth jazz", "soulful belting",
            "monotone"
        ]

        self.bpms = list(range(40, 241, 4))

        # Lists to store multiple selections
        self.selected_themes = []
        self.selected_moods = []
        self.selected_instruments = []
        self.selected_effects = []
        self.selected_settings = []
        self.selected_time_periods = []
        self.selected_cultural_influences = []
        self.selected_narrative_themes = []
        self.selected_lyrical_themes = []
        self.selected_vocal_styles = []

        # Scrollable canvas for GUI
        canvas = Canvas(root)
        scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # GUI Layout
        tk.Label(scrollable_frame, text="Advanced Music Prompt Generator", font=("Arial", 16, "bold")).pack(pady=10)

        input_frame = tk.Frame(scrollable_frame)
        input_frame.pack(pady=10)

        # Movement Name Entry
        tk.Label(input_frame, text="Movement Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="e")
        self.movement_entry = tk.Entry(input_frame, width=20)
        self.movement_entry.grid(row=0, column=1, pady=5, columnspan=2)
        self.movement_entry.insert(0, "I. Dies Irae")

        # Theme Selection
        tk.Label(input_frame, text="Themes:", font=("Arial", 10)).grid(row=1, column=0, sticky="ne")
        theme_frame = tk.Frame(input_frame)
        theme_frame.grid(row=1, column=1, pady=5)
        self.theme_listbox = tk.Listbox(theme_frame, height=8, width=30, selectmode="multiple")
        for theme in self.themes:
            self.theme_listbox.insert(tk.END, theme)
        self.theme_listbox.pack(side=tk.LEFT)
        theme_scroll = tk.Scrollbar(theme_frame, orient="vertical", command=self.theme_listbox.yview)
        theme_scroll.pack(side=tk.RIGHT, fill="y")
        self.theme_listbox.config(yscrollcommand=theme_scroll.set)
        tk.Button(input_frame, text="Add Themes", command=self.add_themes, font=("Arial", 8)).grid(row=1, column=2, padx=5)
        self.theme_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.theme_display.grid(row=1, column=3, pady=5)
        tk.Button(input_frame, text="Clear Themes", command=self.clear_themes, font=("Arial", 8)).grid(row=1, column=4, padx=5)

        # Mood Selection
        tk.Label(input_frame, text="Moods:", font=("Arial", 10)).grid(row=2, column=0, sticky="ne")
        mood_frame = tk.Frame(input_frame)
        mood_frame.grid(row=2, column=1, pady=5)
        self.mood_listbox = tk.Listbox(mood_frame, height=8, width=30, selectmode="multiple")
        for mood in self.moods:
            self.mood_listbox.insert(tk.END, mood)
        self.mood_listbox.pack(side=tk.LEFT)
        mood_scroll = tk.Scrollbar(mood_frame, orient="vertical", command=self.mood_listbox.yview)
        mood_scroll.pack(side=tk.RIGHT, fill="y")
        self.mood_listbox.config(yscrollcommand=mood_scroll.set)
        tk.Button(input_frame, text="Add Moods", command=self.add_moods, font=("Arial", 8)).grid(row=2, column=2, padx=5)
        self.mood_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.mood_display.grid(row=2, column=3, pady=5)
        tk.Button(input_frame, text="Clear Moods", command=self.clear_moods, font=("Arial", 8)).grid(row=2, column=4, padx=5)

        # Instrument Selection
        tk.Label(input_frame, text="Instruments:", font=("Arial", 10)).grid(row=3, column=0, sticky="ne")
        instr_frame = tk.Frame(input_frame)
        instr_frame.grid(row=3, column=1, pady=5)
        self.instr_listbox = tk.Listbox(instr_frame, height=8, width=30, selectmode="multiple")
        for instr in self.instruments:
            self.instr_listbox.insert(tk.END, instr)
        self.instr_listbox.pack(side=tk.LEFT)
        instr_scroll = tk.Scrollbar(instr_frame, orient="vertical", command=self.instr_listbox.yview)
        instr_scroll.pack(side=tk.RIGHT, fill="y")
        self.instr_listbox.config(yscrollcommand=instr_scroll.set)
        tk.Button(input_frame, text="Add Instruments", command=self.add_instruments, font=("Arial", 8)).grid(row=3, column=2, padx=5)
        self.instr_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.instr_display.grid(row=3, column=3, pady=5)
        tk.Button(input_frame, text="Clear Instruments", command=self.clear_instruments, font=("Arial", 8)).grid(row=3, column=4, padx=5)

        # Effect Selection
        tk.Label(input_frame, text="Effects:", font=("Arial", 10)).grid(row=4, column=0, sticky="ne")
        effect_frame = tk.Frame(input_frame)
        effect_frame.grid(row=4, column=1, pady=5)
        self.effect_listbox = tk.Listbox(effect_frame, height=8, width=30, selectmode="multiple")
        for effect in self.effects:
            self.effect_listbox.insert(tk.END, effect)
        self.effect_listbox.pack(side=tk.LEFT)
        effect_scroll = tk.Scrollbar(effect_frame, orient="vertical", command=self.effect_listbox.yview)
        effect_scroll.pack(side=tk.RIGHT, fill="y")
        self.effect_listbox.config(yscrollcommand=effect_scroll.set)
        tk.Button(input_frame, text="Add Effects", command=self.add_effects, font=("Arial", 8)).grid(row=4, column=2, padx=5)
        self.effect_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.effect_display.grid(row=4, column=3, pady=5)
        tk.Button(input_frame, text="Clear Effects", command=self.clear_effects, font=("Arial", 8)).grid(row=4, column=4, padx=5)

        # Setting Selection
        tk.Label(input_frame, text="Settings:", font=("Arial", 10)).grid(row=5, column=0, sticky="ne")
        setting_frame = tk.Frame(input_frame)
        setting_frame.grid(row=5, column=1, pady=5)
        self.setting_listbox = tk.Listbox(setting_frame, height=8, width=30, selectmode="multiple")
        for setting in self.settings:
            self.setting_listbox.insert(tk.END, setting)
        self.setting_listbox.pack(side=tk.LEFT)
        setting_scroll = tk.Scrollbar(setting_frame, orient="vertical", command=self.setting_listbox.yview)
        setting_scroll.pack(side=tk.RIGHT, fill="y")
        self.setting_listbox.config(yscrollcommand=setting_scroll.set)
        tk.Button(input_frame, text="Add Settings", command=self.add_settings, font=("Arial", 8)).grid(row=5, column=2, padx=5)
        self.setting_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.setting_display.grid(row=5, column=3, pady=5)
        tk.Button(input_frame, text="Clear Settings", command=self.clear_settings, font=("Arial", 8)).grid(row=5, column=4, padx=5)

        # Time Period Selection
        tk.Label(input_frame, text="Time Periods:", font=("Arial", 10)).grid(row=6, column=0, sticky="ne")
        time_frame = tk.Frame(input_frame)
        time_frame.grid(row=6, column=1, pady=5)
        self.time_listbox = tk.Listbox(time_frame, height=8, width=30, selectmode="multiple")
        for time in self.time_periods:
            self.time_listbox.insert(tk.END, time)
        self.time_listbox.pack(side=tk.LEFT)
        time_scroll = tk.Scrollbar(time_frame, orient="vertical", command=self.time_listbox.yview)
        time_scroll.pack(side=tk.RIGHT, fill="y")
        self.time_listbox.config(yscrollcommand=time_scroll.set)
        tk.Button(input_frame, text="Add Time Periods", command=self.add_time_periods, font=("Arial", 8)).grid(row=6, column=2, padx=5)
        self.time_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.time_display.grid(row=6, column=3, pady=5)
        tk.Button(input_frame, text="Clear Time Periods", command=self.clear_time_periods, font=("Arial", 8)).grid(row=6, column=4, padx=5)

        # Cultural Influence Selection
        tk.Label(input_frame, text="Cultural Influences:", font=("Arial", 10)).grid(row=7, column=0, sticky="ne")
        culture_frame = tk.Frame(input_frame)
        culture_frame.grid(row=7, column=1, pady=5)
        self.culture_listbox = tk.Listbox(culture_frame, height=8, width=30, selectmode="multiple")
        for culture in self.cultural_influences:
            self.culture_listbox.insert(tk.END, culture)
        self.culture_listbox.pack(side=tk.LEFT)
        culture_scroll = tk.Scrollbar(culture_frame, orient="vertical", command=self.culture_listbox.yview)
        culture_scroll.pack(side=tk.RIGHT, fill="y")
        self.culture_listbox.config(yscrollcommand=culture_scroll.set)
        tk.Button(input_frame, text="Add Cultures", command=self.add_cultural_influences, font=("Arial", 8)).grid(row=7, column=2, padx=5)
        self.culture_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.culture_display.grid(row=7, column=3, pady=5)
        tk.Button(input_frame, text="Clear Cultures", command=self.clear_cultural_influences, font=("Arial", 8)).grid(row=7, column=4, padx=5)

        # Narrative Theme Selection
        tk.Label(input_frame, text="Narrative Themes:", font=("Arial", 10)).grid(row=8, column=0, sticky="ne")
        narrative_frame = tk.Frame(input_frame)
        narrative_frame.grid(row=8, column=1, pady=5)
        self.narrative_listbox = tk.Listbox(narrative_frame, height=8, width=30, selectmode="multiple")
        for narrative in self.narrative_themes:
            self.narrative_listbox.insert(tk.END, narrative)
        self.narrative_listbox.pack(side=tk.LEFT)
        narrative_scroll = tk.Scrollbar(narrative_frame, orient="vertical", command=self.narrative_listbox.yview)
        narrative_scroll.pack(side=tk.RIGHT, fill="y")
        self.narrative_listbox.config(yscrollcommand=narrative_scroll.set)
        tk.Button(input_frame, text="Add Narratives", command=self.add_narrative_themes, font=("Arial", 8)).grid(row=8, column=2, padx=5)
        self.narrative_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.narrative_display.grid(row=8, column=3, pady=5)
        tk.Button(input_frame, text="Clear Narratives", command=self.clear_narrative_themes, font=("Arial", 8)).grid(row=8, column=4, padx=5)

        # Lyrical Theme Selection
        tk.Label(input_frame, text="Lyrical Themes:", font=("Arial", 10)).grid(row=9, column=0, sticky="ne")
        lyrical_frame = tk.Frame(input_frame)
        lyrical_frame.grid(row=9, column=1, pady=5)
        self.lyrical_listbox = tk.Listbox(lyrical_frame, height=8, width=30, selectmode="multiple")
        for lyrical in self.lyrical_themes:
            self.lyrical_listbox.insert(tk.END, lyrical)
        self.lyrical_listbox.pack(side=tk.LEFT)
        lyrical_scroll = tk.Scrollbar(lyrical_frame, orient="vertical", command=self.lyrical_listbox.yview)
        lyrical_scroll.pack(side=tk.RIGHT, fill="y")
        self.lyrical_listbox.config(yscrollcommand=lyrical_scroll.set)
        tk.Button(input_frame, text="Add Lyrical Themes", command=self.add_lyrical_themes, font=("Arial", 8)).grid(row=9, column=2, padx=5)
        self.lyrical_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.lyrical_display.grid(row=9, column=3, pady=5)
        tk.Button(input_frame, text="Clear Lyrical Themes", command=self.clear_lyrical_themes, font=("Arial", 8)).grid(row=9, column=4, padx=5)

        # Vocal Style Selection
        tk.Label(input_frame, text="Vocal Styles:", font=("Arial", 10)).grid(row=10, column=0, sticky="ne")
        vocal_frame = tk.Frame(input_frame)
        vocal_frame.grid(row=10, column=1, pady=5)
        self.vocal_listbox = tk.Listbox(vocal_frame, height=8, width=30, selectmode="multiple")
        for vocal in self.vocal_styles:
            self.vocal_listbox.insert(tk.END, vocal)
        self.vocal_listbox.pack(side=tk.LEFT)
        vocal_scroll = tk.Scrollbar(vocal_frame, orient="vertical", command=self.vocal_listbox.yview)
        vocal_scroll.pack(side=tk.RIGHT, fill="y")
        self.vocal_listbox.config(yscrollcommand=vocal_scroll.set)
        tk.Button(input_frame, text="Add Vocal Styles", command=self.add_vocal_styles, font=("Arial", 8)).grid(row=10, column=2, padx=5)
        self.vocal_display = tk.Label(input_frame, text="Selected: None", font=("Arial", 8), wraplength=200)
        self.vocal_display.grid(row=10, column=3, pady=5)
        tk.Button(input_frame, text="Clear Vocal Styles", command=self.clear_vocal_styles, font=("Arial", 8)).grid(row=10, column=4, padx=5)

        # BPM Entry
        tk.Label(input_frame, text="BPM (leave blank for random):", font=("Arial", 10)).grid(row=11, column=0, sticky="e")
        self.bpm_entry = tk.Entry(input_frame, width=10)
        self.bpm_entry.grid(row=11, column=1, pady=5)

        # Random Toggle Checkbox
        self.random_var = tk.BooleanVar(value=True)
        tk.Checkbutton(scrollable_frame, text="Use Random Values (ignore selections if checked)",
                       variable=self.random_var, font=("Arial", 10)).pack(pady=10)

        # Prompt Display
        self.prompt_text = tk.Text(scrollable_frame, height=8, width=80, wrap="word", font=("Arial", 10))
        self.prompt_text.pack(pady=20)
        self.prompt_text.insert(tk.END, "Click 'Generate' to create a prompt!")
        self.prompt_text.config(state="disabled")

        # Buttons Frame
        button_frame = tk.Frame(scrollable_frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Generate Prompt", command=self.generate_prompt,
                  font=("Arial", 12), bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Copy to Clipboard", command=self.copy_prompt,
                  font=("Arial", 12), bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Save to File", command=self.save_prompt,
                  font=("Arial", 12), bg="#FF9800", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Quit", command=root.quit,
                  font=("Arial", 12), bg="#F44336", fg="white").grid(row=0, column=3, padx=5)

    # Clear methods
    def clear_themes(self):
        self.selected_themes.clear()
        self.theme_display.config(text="Selected: None")

    def clear_moods(self):
        self.selected_moods.clear()
        self.mood_display.config(text="Selected: None")

    def clear_instruments(self):
        self.selected_instruments.clear()
        self.instr_display.config(text="Selected: None")

    def clear_effects(self):
        self.selected_effects.clear()
        self.effect_display.config(text="Selected: None")

    def clear_settings(self):
        self.selected_settings.clear()
        self.setting_display.config(text="Selected: None")

    def clear_time_periods(self):
        self.selected_time_periods.clear()
        self.time_display.config(text="Selected: None")

    def clear_cultural_influences(self):
        self.selected_cultural_influences.clear()
        self.culture_display.config(text="Selected: None")

    def clear_narrative_themes(self):
        self.selected_narrative_themes.clear()
        self.narrative_display.config(text="Selected: None")

    def clear_lyrical_themes(self):
        self.selected_lyrical_themes.clear()
        self.lyrical_display.config(text="Selected: None")

    def clear_vocal_styles(self):
        self.selected_vocal_styles.clear()
        self.vocal_display.config(text="Selected: None")

    # Methods to add multiple selections from listboxes
    def add_themes(self):
        selected_indices = self.theme_listbox.curselection()
        for idx in selected_indices:
            theme = self.theme_listbox.get(idx)
            if theme not in self.selected_themes:
                self.selected_themes.append(theme)
        self.theme_display.config(text=f"Selected: {', '.join(self.selected_themes)}" if self.selected_themes else "Selected: None")

    def add_moods(self):
        selected_indices = self.mood_listbox.curselection()
        for idx in selected_indices:
            mood = self.mood_listbox.get(idx)
            if mood not in self.selected_moods:
                self.selected_moods.append(mood)
        self.mood_display.config(text=f"Selected: {', '.join(self.selected_moods)}" if self.selected_moods else "Selected: None")

    def add_instruments(self):
        selected_indices = self.instr_listbox.curselection()
        for idx in selected_indices:
            instr = self.instr_listbox.get(idx)
            if instr not in self.selected_instruments:
                self.selected_instruments.append(instr)
        self.instr_display.config(text=f"Selected: {', '.join(self.selected_instruments)}" if self.selected_instruments else "Selected: None")

    def add_effects(self):
        selected_indices = self.effect_listbox.curselection()
        for idx in selected_indices:
            effect = self.effect_listbox.get(idx)
            if effect not in self.selected_effects:
                self.selected_effects.append(effect)
        self.effect_display.config(text=f"Selected: {', '.join(self.selected_effects)}" if self.selected_effects else "Selected: None")

    def add_settings(self):
        selected_indices = self.setting_listbox.curselection()
        for idx in selected_indices:
            setting = self.setting_listbox.get(idx)
            if setting not in self.selected_settings:
                self.selected_settings.append(setting)
        self.setting_display.config(text=f"Selected: {', '.join(self.selected_settings)}" if self.selected_settings else "Selected: None")

    def add_time_periods(self):
        selected_indices = self.time_listbox.curselection()
        for idx in selected_indices:
            time = self.time_listbox.get(idx)
            if time not in self.selected_time_periods:
                self.selected_time_periods.append(time)
        self.time_display.config(text=f"Selected: {', '.join(self.selected_time_periods)}" if self.selected_time_periods else "Selected: None")

    def add_cultural_influences(self):
        selected_indices = self.culture_listbox.curselection()
        for idx in selected_indices:
            culture = self.culture_listbox.get(idx)
            if culture not in self.selected_cultural_influences:
                self.selected_cultural_influences.append(culture)
        self.culture_display.config(text=f"Selected: {', '.join(self.selected_cultural_influences)}" if self.selected_cultural_influences else "Selected: None")

    def add_narrative_themes(self):
        selected_indices = self.narrative_listbox.curselection()
        for idx in selected_indices:
            narrative = self.narrative_listbox.get(idx)
            if narrative not in self.selected_narrative_themes:
                self.selected_narrative_themes.append(narrative)
        self.narrative_display.config(text=f"Selected: {', '.join(self.selected_narrative_themes)}" if self.selected_narrative_themes else "Selected: None")

    def add_lyrical_themes(self):
        selected_indices = self.lyrical_listbox.curselection()
        for idx in selected_indices:
            lyrical = self.lyrical_listbox.get(idx)
            if lyrical not in self.selected_lyrical_themes:
                self.selected_lyrical_themes.append(lyrical)
        self.lyrical_display.config(text=f"Selected: {', '.join(self.selected_lyrical_themes)}" if self.selected_lyrical_themes else "Selected: None")

    def add_vocal_styles(self):
        selected_indices = self.vocal_listbox.curselection()
        for idx in selected_indices:
            vocal = self.vocal_listbox.get(idx)
            if vocal not in self.selected_vocal_styles:
                self.selected_vocal_styles.append(vocal)
        self.vocal_display.config(text=f"Selected: {', '.join(self.selected_vocal_styles)}" if self.selected_vocal_styles else "Selected: None")

    def generate_prompt(self):
        movement = self.movement_entry.get() if self.movement_entry.get() else "Unnamed Movement"

        if self.random_var.get():
            num_themes = random.randint(1, 2)
            num_moods = random.randint(1, 2)
            num_instr = random.randint(1, 2)
            num_effects = random.randint(1, 2)
            num_settings = random.randint(1, 2)
            num_lyrical = random.randint(1, 1)
            num_vocal = random.randint(1, 1)
            num_time = random.randint(1, 1)
            num_culture = random.randint(1, 1)
            num_narrative = random.randint(1, 1)
            theme = "-".join(random.sample(self.themes, num_themes))
            mood = "-".join(random.sample(self.moods, num_moods))
            instr = ", ".join(random.sample(self.instruments, num_instr))
            effect = ", ".join(random.sample(self.effects, num_effects))
            setting = ", ".join(random.sample(self.settings, num_settings))
            lyrical = random.choice(self.lyrical_themes)
            vocal = random.choice(self.vocal_styles)
            time = random.choice(self.time_periods)
            culture = random.choice(self.cultural_influences)
            narrative = random.choice(self.narrative_themes)
            bpm = random.choice(self.bpms)
        else:
            if not any([self.selected_themes, self.selected_moods, self.selected_instruments,
                        self.selected_effects, self.selected_settings, self.selected_time_periods,
                        self.selected_cultural_influences, self.selected_narrative_themes,
                        self.selected_lyrical_themes, self.selected_vocal_styles]):
                messagebox.showwarning("No Selections", "Please select at least one item or enable random mode.")
                return
            theme = "-".join(self.selected_themes[:2]) if self.selected_themes else random.choice(self.themes)
            mood = "-".join(self.selected_moods[:2]) if self.selected_moods else random.choice(self.moods)
            instr = ", ".join(self.selected_instruments[:2]) if self.selected_instruments else random.choice(self.instruments)
            effect = ", ".join(self.selected_effects[:2]) if self.selected_effects else random.choice(self.effects)
            setting = ", ".join(self.selected_settings[:2]) if self.selected_settings else random.choice(self.settings)
            lyrical = self.selected_lyrical_themes[0] if self.selected_lyrical_themes else random.choice(self.lyrical_themes)
            vocal = self.selected_vocal_styles[0] if self.selected_vocal_styles else random.choice(self.vocal_styles)
            time = self.selected_time_periods[0] if self.selected_time_periods else random.choice(self.time_periods)
            culture = self.selected_cultural_influences[0] if self.selected_cultural_influences else random.choice(self.cultural_influences)
            narrative = self.selected_narrative_themes[0] if self.selected_narrative_themes else random.choice(self.narrative_themes)
            bpm_input = self.bpm_entry.get()
            try:
                bpm = int(bpm_input) if bpm_input else random.choice(self.bpms)
                if not (40 <= bpm <= 240):
                    raise ValueError("BPM out of range")
            except ValueError:
                bpm = random.choice(self.bpms)
                messagebox.showwarning("Invalid BPM", "BPM must be a number between 40 and 240; using random value.")

        prompt = (
            f"{movement}: {theme} with {instr}, {mood} atmosphere, {bpm}BPM, "
            f"{effect}, set in {setting}, from the {time} era, "
            f"influenced by {culture} culture, with a {narrative} narrative. "
            f"Lyrics focus on {lyrical}, delivered in a {vocal} vocal style."
        )

        self.prompt_text.config(state="normal")
        self.prompt_text.delete(1.0, tk.END)
        self.prompt_text.insert(tk.END, prompt)
        self.prompt_text.config(state="disabled")
        self.current_prompt = prompt

    def copy_prompt(self):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_prompt)
            messagebox.showinfo("Success", "Prompt copied to clipboard!")
        except AttributeError:
            messagebox.showwarning("Error", "Generate a prompt first!")

    def save_prompt(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                with open(file_path, "a") as f:
                    f.write(self.current_prompt + "\n")
                messagebox.showinfo("Success", f"Prompt saved to {file_path}!")
        except AttributeError:
            messagebox.showwarning("Error", "Generate a prompt first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptMakerGUI(root)
    root.mainloop()