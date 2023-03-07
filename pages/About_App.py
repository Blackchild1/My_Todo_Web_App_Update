import streamlit as st


st.set_page_config(
    page_title="About App",
    page_icon="✍",
    layout="wide"
)


st.write("# About App")
st.text(
    """
    The name of the app is "Top-G To-Do List".
    It is basically for adding and deleting to-do. 

    """
)
st.header("How To Add To-Do")
st.text(
    """
    This is basically a to-do app where you can add list of things you 
    wish to accomplish in a day or two so, you basically do that by
    adding your to-do in the "add new to-do" box, press enter then write 
    a full detailed note on your to-do in "notes" below the list of to-do box,
    then press enter. 
    """
)
st.header("How To Read More About Your To-Do ")
st.text(
    """
        👈 You can always read details on your to-do using the sidebar to navigate to the
        "My To-Do Documentation" page.    

    """
)

st.text(
    """ 
    The "My To-Do Documentation" page contains your to-do as an header 
    and your to-do notes as a sub-header for you to read anytime.
    
    """
)
st.header("How To Delete To-Do")
st.text(
    """
    When you click on the check box beside each to-do in the home page,
    it will automatically make the to-do you click on move to the completed
    to-do list which you can find in "Completed To-Do" tab immediately beside 
    the "My To-Do List" tab.
    click on it and confirm it yourself.      
     
    """
 )

st.text(
    """
    If you wish to completely delete your to-do, go to the "Completed To-Do" 
    tab, from there:
    click on the check box beside each to-do in that tab, it will automatically
    delete the to-do finally from the list of your to-do which means you 
    have absolutely completed that particular todo.
    Thank You. 
 
    """
)

st.text(
        """
        I hope you enjoy the app features, we are still working 
        on the interface currently.
        """
)
