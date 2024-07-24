import streamlit as st

if not st.session_state.login or st.session_state.accessLevel == "admin":
    st.error("You are not logged in or you doesn't have access. You need to login to access this page.")
    st.stop()

with st.sidebar:
    st.html("""
            <div style="margin-left:30px">
                <img src='https://www.jsw.in/sites/all/themes/jsw_theme/images/logos/jsw.png'/>
                <p>Occupational Health Center</p>
            </div>
            """)
    st.header("Navigation")
    st.page_link("pages/dashboard.py",label="Dashboard",icon=":material/dashboard:")
    st.page_link("pages/new_visits.py",label="New Visit",icon=":material/settings:")
    st.page_link("pages/events_and_camps.py",label="Events and Camps",icon=":material/event:")
    st.page_link("pages/records_and_filter.py",label="Records and Filters",icon=":material/tune:")
    st.page_link("pages/mockdrill.py",label="Mock Drill",icon=":material/shield:")
    st.page_link("pages/appointment.py",label="Appointment",icon=":material/event_available:")
    
    st.divider()
    st.write(f"Logged in as : {st.session_state.accessLevel}")

    if st.button("Logout"):
        st.session_state.accessLevel = None
        st.session_state.login = False
        st.switch_page("main.py")

st.title("Dashboard")