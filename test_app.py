from app import app

def test_dash_app_layout_and_elements(dash_duo):
    # Start the server just once
    dash_duo.start_server(app)
    
    # 1. Test that the Header is present
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text == "Soul Foods: Pink Morsel Sales Visualizer"
    
    # 2. Test that the Visualization (the graph) is present
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    
    # 3. Test that the Region Picker (the radio buttons) is present
    dash_duo.wait_for_element("#region-filter", timeout=10)