import streamlit as st
import logging

def load_svg(file_path):
    """Carrega o conteúdo de um arquivo SVG ou retorna um ícone padrão se falhar."""
    default_icon = "bar-chart-fill"  # Ícone padrão

    try:
        with open(file_path, "r") as svg_file:
            return svg_file.read()  # Lê o conteúdo do arquivo SVG
    except FileNotFoundError:
        logging.warning(f"SVG file not found: {file_path}. Using default icon.")
        return default_icon
    except Exception as e:
        logging.error(f"Error loading SVG: {e}. Using default icon.")
        return default_icon
