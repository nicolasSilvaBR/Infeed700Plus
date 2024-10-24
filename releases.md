# Version 1.0.0 (latest)

**Release date**: January 1, 2025

## Table of Contents
1. [Highlights](#highlights)
2. [Notable Changes](#notable-changes)
3. [Other Changes](#other-changes)

## Highlights
- **Introducing** `st.experimental_audio_input` to let users record with their microphones!
- `st.pydeck_chart` can now return selection events!

## Notable Changes
- `st.button`, `st.download_button`, `st.form_submit_button`, `st.link_button`, and `st.popover` each have a new parameter to add an icon.
- `st.logo` has a new parameter to adjust the size of your logo.
- `st.navigation` lets you display an always-expanded or collapsible menu using a new `expanded` parameter.
- You can set height and width for `st.map` and `st.pydeck_chart`.
- Form submission behavior can be configured with a new `enter_to_submit` parameter (#9480, #7538, #9406, #8042).
- A new config option, `server.disconnectedSessionTTL`, lets you set a minimum time before a disconnected session is cleaned up (#9179).
- Dataframes support multi-index headers (#9483, #6319).

## Other Changes
- Widget keys appear as HTML classes in the DOM with an `st-key-` prefix (#9295, #5437, #3888).
- The `StreamlitAPIException` class has been extended into more specific exceptions for some of the most common errors (#9318).

