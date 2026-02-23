from domain.models import Card


class DeckRepository:

    def load_deck(self) -> list[Card]:

        raw_cards = [
            (1, "THE VOID", "Cosmic Origin", "Absence is the final fact"),
            (2, "GENESIS", "Cosmic Origin", "Silence fractures before creation"),
            (3, "ORIGIN", "Cosmic Origin", "The origin is never erased"),
            (4, "VOID-STAR", "Cosmic Origin", "Stillness accumulates until explosion"),
            (5, "SINGULARITY", "Cosmic Origin", "Complexity collapses to core"),

            (6, "GRAVITY", "Law & Structure", "Weight defines decision"),
            (7, "ORDER", "Law & Structure", "Structure decays under control"),
            (8, "CHAOS", "Law & Structure", "All systems expire"),
            (9, "SYMMETRY", "Law & Structure", "Every system has its opposite"),
            (10, "PARADOX", "Law & Structure", "Truth contains contradiction"),

            (11, "FLOW", "Movement & Force", "Action transforms the actor"),
            (12, "IMPACT", "Movement & Force", "Force does not return unchanged"),
            (13, "RESONANCE", "Movement & Force", "What vibrates together expands"),
            (14, "PULSE", "Movement & Force", "Rhythm is pause and restart"),
            (15, "ENTROPY", "Movement & Force", "Decay is law"),

            (16, "THRESHOLD", "Boundary & Transition", "A boundary demands a cut"),
            (17, "GATEWAY", "Boundary & Transition", "Every passage has a price"),
            (18, "HORIZON", "Boundary & Transition", "The horizon always moves"),
            (19, "ASCENT", "Boundary & Transition", "Elevation changes identity"),
            (20, "ASCENSION", "Boundary & Transition", "Weight determines rise"),

            (21, "SHADOW", "Light & Shadow", "Light creates shadow"),
            (22, "PRISM", "Light & Shadow", "Purity integrates all colors"),
            (23, "LUMINANCE", "Light & Shadow", "Brightness has cost"),
            (24, "ECHO", "Light & Shadow", "Source defines reflection"),
            (25, "SOURCE-ECHO", "Light & Shadow", "Initiation calls response"),

            (26, "ALLIANCE", "Human Field", "Need connects power"),
            (27, "DISCORD", "Human Field", "Difference is natural law"),
            (28, "FRACTURE", "Human Field", "Cracks reveal weakness"),
            (29, "ANCHOR", "Human Field", "Stillness requires grounding"),
            (30, "STILLNESS", "Human Field", "Movement roots in silence"),

            (31, "AURA", "Meta Field", "Energy outlives form"),
            (32, "PRESENCE", "Meta Field", "The witness remains"),
            (33, "AEON", "Meta Field", "Time judges all"),
            (34, "NOVA", "Meta Field", "Fuel becomes revelation"),
            (35, "INFINITY", "Meta Field", "Limits are illusion"),
            (36, "ECLIPSE", "Meta Field", "Even law has shadow"),
        ]

        return [
            Card(
                name=name,
                archetype=archetype,
                meaning=meaning
            )
            for _, name, archetype, meaning in raw_cards
        ]
