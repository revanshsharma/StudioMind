from google.adk.agents import Agent

root_agent = Agent(
    name="studiomind",
    model="gemini-3-flash-preview",
    description="StudioMind is an AI assistant for film pre-production.",
    instruction="""
    You are StudioMind, an AI assistant for filmmakers.

    Help users understand screenplays, production requirements,
    filming locations, and visual development.

    For now, simply answer questions about film pre-production.
    """
)