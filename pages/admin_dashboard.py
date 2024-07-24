import streamlit as st

if not st.session_state.login or st.session_state.accessLevel != "admin":
    st.error("You are not logged in. You need to login to access this page.")
    st.stop()

with st.sidebar:
    st.html("""
            <div style="margin-left:30px">
                <img src='https://www.jsw.in/sites/all/themes/jsw_theme/images/logos/jsw.png'/>
                <p>Occupational Health Center</p>
            </div>
            """)
    st.header("Navigation")
    st.page_link("pages/admin_dashboard.py",label="Dashboard",icon=":material/dashboard:")
    st.page_link("pages/add_doc.py",label="Add Doctor",icon=":material/person_add:")
    st.page_link("pages/add_nurse.py",label="Add Nurse",icon=":material/person_add:")
    st.page_link("pages/add_emp.py",label="Add Employee",icon=":material/group_add:")
    st.page_link("pages/add_reference_range.py",label="Add Reference Range",icon=":material/add_link:")
    st.page_link("pages/view_staffs.py",label="View Staffs",icon=":material/view_list:")

    st.divider()
    st.header("Login details")
    st.write(f"Logged in as : {st.session_state.accessLevel}")

    if st.button("Logout"):
        st.session_state.accessLevel = None
        st.session_state.login = False
        st.switch_page("main.py")


st.title("Admin Dashboard")

st.write("Welcome to the admin dashboard")