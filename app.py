import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from utils.helpers import load_fibers_data
import pathlib

# Set page configuration
st.set_page_config(
    page_title="Textile Fiber Explorer",
    page_icon="🧵",
    layout="wide"
)

# Load custom CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS
load_css()

# Load fiber data
fibers_data = load_fibers_data()

def main():
    # Header
    st.title("🧵 Textile Fiber Explorer")
    st.markdown("Explore textile fibers from properties to applications and global production")
    
    # Sidebar for navigation
    with st.sidebar:
        st.header("Navigation")
        nav_option = st.radio(
            "Choose Section",
            ["🏠 Home", "🔍 Fiber Explorer", "📊 Global Production", "ℹ️ About"]
        )
        
        if nav_option == "🔍 Fiber Explorer":
            st.header("Select Fiber")
            fiber_list = [fiber["name"] for fiber in fibers_data]
            selected_fiber_name = st.selectbox(
                "Choose a fiber to explore",
                fiber_list,
                index=0
            )
        
        st.divider()
        st.markdown("### Quick Stats")
        st.write(f"📁 **Fibers in database:** {len(fibers_data)}")
        st.write("🌍 **Data covers:** Properties, Applications, Production")
        st.write("🛠️ **Built with:** Streamlit + Python")
    
    # Home Page
    if nav_option == "🏠 Home":
        show_home_page(fibers_data)
    
    # Fiber Explorer
    elif nav_option == "🔍 Fiber Explorer":
        selected_fiber = next((f for f in fibers_data if f["name"] == selected_fiber_name), None)
        if selected_fiber:
            show_fiber_details(selected_fiber)
        else:
            st.error("Fiber not found in database")
    
    # Global Production
    elif nav_option == "📊 Global Production":
        show_global_production(fibers_data)
    
    # About Page
    elif nav_option == "ℹ️ About":
        show_about_page()

def show_home_page(fibers_data):
    """Display the home page"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Welcome to Fiber Explorer")
        st.markdown("""
        This interactive tool helps you explore various textile fibers:
        
        - **Learn about fiber properties**
        - **Discover applications and uses**
        - **Compare advantages and limitations**
        - **See global production statistics**
        - **Get interesting fiber facts**
        
        Use the sidebar to navigate through different sections.
        """)
        
        # Quick fiber summary
        st.subheader("Available Fibers")
        fiber_df = pd.DataFrame(fibers_data)[['name', 'type', 'sustainability']]
        st.dataframe(fiber_df, use_container_width=True, hide_index=True)
    
    with col2:
        # Fiber type distribution
        fiber_types = [f["type"] for f in fibers_data]
        type_counts = pd.Series(fiber_types).value_counts()
        
        fig = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title="Fiber Type Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Quick search
        st.subheader("Quick Search")
        search_term = st.text_input("Search for a fiber:")
        if search_term:
            matching_fibers = [f for f in fibers_data if search_term.lower() in f["name"].lower()]
            if matching_fibers:
                for fiber in matching_fibers[:3]:
                    st.info(f"**{fiber['name']}** - {fiber['type']}")
            else:
                st.warning("No fibers found matching your search")

def show_fiber_details(fiber):
    """Display detailed information about a selected fiber"""
    st.header(f"🧵 {fiber['name']}")
    
    # Basic info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Fiber Type", fiber["type"])
    with col2:
        st.metric("Sustainability", fiber["sustainability"])
    with col3:
        st.metric("Common Uses", len(fiber["applications"]))
    
    st.divider()
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Properties", 
        "✅ Advantages", 
        "❌ Limitations", 
        "👕 Applications", 
        "🇺🇳 Production"
    ])
    
    # Properties Tab
    with tab1:
        st.subheader("Key Properties")
        properties_df = pd.DataFrame({
            "Property": fiber["properties"].keys(),
            "Value": fiber["properties"].values()
        })
        st.dataframe(properties_df, use_container_width=True, hide_index=True)
        
        # Property bar chart
        fig = px.bar(
            properties_df,
            x="Property",
            y="Value",
            title=f"{fiber['name']} Properties",
            color_discrete_sequence=['#2E86AB']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Advantages Tab
    with tab2:
        st.subheader("Advantages")
        for advantage in fiber["advantages"]:
            st.success(f"✅ {advantage}")
    
    # Limitations Tab
    with tab3:
        st.subheader("Limitations")
        for limitation in fiber["limitations"]:
            st.error(f"❌ {limitation}")
    
    # Applications Tab
    with tab4:
        st.subheader("Common End Uses")
        col1_app, col2_app = st.columns(2)
        
        with col1_app:
            for application in fiber["applications"][:len(fiber["applications"])//2]:
                st.write(f"👕 **{application}**")
        
        with col2_app:
            for application in fiber["applications"][len(fiber["applications"])//2:]:
                st.write(f"👕 **{application}**")
        
        # Application categories
        st.subheader("Application Categories")
        application_categories = {
            "Apparel": ["T-shirts", "Dresses", "Jeans", "Activewear"],
            "Home Textiles": ["Bedding", "Curtains", "Towels", "Upholstery"],
            "Technical": ["Medical textiles", "Geotextiles", "Protective clothing"]
        }
        
        for category, items in application_categories.items():
            if any(item in fiber["applications"] for item in items):
                st.info(f"**{category}**: Used in {', '.join([i for i in items if i in fiber['applications']])}")
    
    # Production Tab
    with tab5:
        st.subheader("Top 3 Producing Countries")
        df_countries = pd.DataFrame({
            "Country": fiber["production_countries"],
            "Production Share (%)": fiber["production_shares"]
        })
        
        # Bar chart for production
        fig_prod = px.bar(
            df_countries,
            x="Country",
            y="Production Share (%)",
            title=f"{fiber['name']} Global Production",
            color="Country",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_prod, use_container_width=True)
        
        # Display production data
        st.dataframe(df_countries, use_container_width=True, hide_index=True)
        
        # Trend line (simulated)
        st.subheader("Production Trend (Simulated)")
        years = list(range(2015, 2024))
        trend = [fiber["production_trend"] * (1 + 0.05*i) for i in range(len(years))]
        
        fig_trend = px.line(
            x=years,
            y=trend,
            title="Production Trend Over Years",
            labels={"x": "Year", "y": "Production Index"}
        )
        st.plotly_chart(fig_trend, use_container_width=True)
    
    st.divider()
    
    # Did You Know Section
    st.subheader("💡 Did You Know?")
    st.info(f"**{fiber['did_you_know']}**")
    
    # Comparison section
    st.subheader("Compare with Other Fibers")
    compare_fibers = st.multiselect(
        "Select fibers to compare:",
        [f["name"] for f in fibers_data if f["name"] != fiber["name"]],
        default=[f["name"] for f in fibers_data if f["name"] != fiber["name"]][:2]
    )
    
    if compare_fibers:
        compare_data = []
        for f_name in compare_fibers:
            f_data = next((f for f in fibers_data if f["name"] == f_name), None)
            if f_data:
                compare_data.append({
                    "Fiber": f_name,
                    "Type": f_data["type"],
                    "Tensile Strength": f_data["properties"].get("tensile_strength", 0),
                    "Moisture Absorption": f_data["properties"].get("moisture_absorption", 0),
                    "Sustainability": f_data["sustainability"]
                })
        
        if compare_data:
            compare_df = pd.DataFrame(compare_data)
            st.dataframe(compare_df, use_container_width=True)

def show_global_production(fibers_data):
    """Display global production statistics"""
    st.header("🌍 Global Fiber Production")
    
    # Prepare production data
    production_data = []
    for fiber in fibers_data:
        total_production = sum(fiber["production_shares"])
        production_data.append({
            "Fiber": fiber["name"],
            "Type": fiber["type"],
            "Total Production Index": total_production,
            "Top Producer": fiber["production_countries"][0],
            "Sustainability": fiber["sustainability"]
        })
    
    production_df = pd.DataFrame(production_data)
    
    # Production overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Total Production by Fiber")
        fig_total = px.bar(
            production_df,
            x="Fiber",
            y="Total Production Index",
            color="Type",
            title="Global Production Distribution"
        )
        st.plotly_chart(fig_total, use_container_width=True)
    
    with col2:
        st.subheader("Production by Fiber Type")
        type_production = production_df.groupby("Type")["Total Production Index"].sum().reset_index()
        fig_type = px.pie(
            type_production,
            values="Total Production Index",
            names="Type",
            title="Production by Fiber Type"
        )
        st.plotly_chart(fig_type, use_container_width=True)
    
    # Detailed table
    st.subheader("Detailed Production Data")
    st.dataframe(production_df, use_container_width=True)
    
    # Sustainability score
    st.subheader("Sustainability Comparison")
    sustainability_data = production_df[["Fiber", "Sustainability", "Total Production Index"]]
    fig_sustainability = px.scatter(
        sustainability_data,
        x="Total Production Index",
        y="Sustainability",
        size="Total Production Index",
        color="Fiber",
        hover_name="Fiber",
        title="Production vs Sustainability"
    )
    st.plotly_chart(fig_sustainability, use_container_width=True)

def show_about_page():
    """Display about page"""
    st.header("About Textile Fiber Explorer")
    
    st.markdown("""
    ### 📚 Project Overview
    
    **Textile Fiber Explorer** is an interactive web application designed to help students,
    researchers, and enthusiasts explore various textile fibers through an intuitive interface.
    
    ### ✨ Features
    
    1. **Comprehensive Fiber Database** - Detailed information on various textile fibers
    2. **Interactive Charts** - Visual representation of properties and production data
    3. **Educational Content** - Advantage/limitation analysis and real-world applications
    4. **Global Production Data** - Insights into production statistics by country
    5. **Comparison Tools** - Side-by-side comparison of different fibers
    
    ### 🛠️ Technology Stack
    
    - **Frontend**: Streamlit
    - **Backend**: Python
    - **Data Visualization**: Plotly
    - **Data Storage**: JSON files
    - **Deployment**: Streamlit Cloud / GitHub
    
    ### 📊 Data Sources
    
    The application uses curated data including:
    - Fiber properties (tensile strength, moisture absorption, elasticity)
    - Application domains (apparel, home textiles, technical textiles)
    - Global production statistics
    - Sustainability ratings
    
    ### 👥 Team
    
    This project was developed as an educational tool for textile engineering students.
    
    ### 📞 Contact
    
    For suggestions or contributions, please visit the GitHub repository.
    """)
    
    st.divider()
    
    # GitHub link
    st.markdown("### 🔗 GitHub Repository")
    st.code("https://github.com/yourusername/textile-fiber-explorer", language="bash")
    
    # How to run locally
    st.markdown("### 🚀 How to Run Locally")
    st.code("""
    git clone https://github.com/yourusername/textile-fiber-explorer.git
    cd textile-fiber-explorer
    pip install -r requirements.txt
    streamlit run app.py
    """, language="bash")

if __name__ == "__main__":
    main()
