import streamlit as st

# Function to display the footer
def display_footer():
    """Display footer with custom CSS at the bottom of the sidebar."""
    st.markdown(
        """
        <style>
            /* Style for the footer to position it at the bottom of the sidebar */
            .sidebar-content {
                display: flex;
                flex-direction: column;
                height: 100%;
            }
            .footer {
                margin-top: auto;
                padding: 20px 0;
                text-align: center;
                font-size: 12px;
                color: #555;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="footer">
            <p>
                <a href="http://10.202.2.22:8503/" target="_blank">Data Lab</a> | 
                <a href="Http://10.202.2.22:8504/" target="_blank">Support</a> | 
                <a href="https://icmcsl.com/contact/" target="_blank">Contact Us</a> |
                <a href="releases.py" target="_blank">Releases</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )