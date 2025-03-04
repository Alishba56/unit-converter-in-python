import streamlit as st

import os


class UnitConverter:
    def __init__(self):
        self.length_units = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }
        
        self.weight_units = {
            'mg': 0.000001,
            'g': 0.001,
            'kg': 1.0,
            'oz': 0.0283495,
            'lb': 0.453592,
            'ton': 907.185
        }
        
        self.volume_units = {
            'ml': 0.001,
            'l': 1.0,
            'gal': 3.78541,
            'qt': 0.946353,
            'pt': 0.473176,
            'fl_oz': 0.0295735
        }
        
        self.unit_names = {
            'mm': 'millimeters',
            'cm': 'centimeters',
            'm': 'meters',
            'km': 'kilometers',
            'in': 'inches',
            'ft': 'feet',
            'yd': 'yards',
            'mi': 'miles',
            'mg': 'milligrams',
            'g': 'grams',
            'kg': 'kilograms',
            'oz': 'ounces',
            'lb': 'pounds',
            'ton': 'tons',
            'ml': 'milliliters',
            'l': 'liters',
            'gal': 'gallons',
            'qt': 'quarts',
            'pt': 'pints',
            'fl_oz': 'fluid ounces',
            'C': 'Celsius',
            'F': 'Fahrenheit',
            'K': 'Kelvin'
        }
    
    def convert_length(self, value, from_unit, to_unit):
        meters = value * self.length_units[from_unit]
        result = meters / self.length_units[to_unit]
        return result
    
    def convert_weight(self, value, from_unit, to_unit):
        kilograms = value * self.weight_units[from_unit]
        result = kilograms / self.weight_units[to_unit]
        return result
    
    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == 'C':
            celsius = value
        elif from_unit == 'F':
            celsius = (value - 32) * 5/9
        elif from_unit == 'K':
            celsius = value - 273.15
        
        if to_unit == 'C':
            return celsius
        elif to_unit == 'F':
            return (celsius * 9/5) + 32
        elif to_unit == 'K':
            return celsius + 273.15
    
    def convert_volume(self, value, from_unit, to_unit):
        liters = value * self.volume_units[from_unit]
        result = liters / self.volume_units[to_unit]
        return result
    
    def convert(self, value, from_unit, to_unit, measurement_type):
        if measurement_type == 'length':
            return self.convert_length(value, from_unit, to_unit)
        elif measurement_type == 'weight':
            return self.convert_weight(value, from_unit, to_unit)
        elif measurement_type == 'temperature':
            return self.convert_temperature(value, from_unit, to_unit)
        elif measurement_type == 'volume':
            return self.convert_volume(value, from_unit, to_unit)
    
    def get_unit_name(self, unit_code):
        return self.unit_names.get(unit_code, unit_code)
    
    def get_units_for_type(self, measurement_type):
        if measurement_type == 'length':
            return self.length_units.keys()
        elif measurement_type == 'weight':
            return self.weight_units.keys()
        elif measurement_type == 'temperature':
            return ['C', 'F', 'K']
        elif measurement_type == 'volume':
            return self.volume_units.keys()
        return []
    
    def format_unit_option(self, unit):
        name = self.get_unit_name(unit)
        return f"{name} ({unit})"


def main():
    st.set_page_config(
        page_title="Unit Converter",
        page_icon="🔄",
        layout="centered"
    )
    
    converter = UnitConverter()
    
    st.title("📏 Unit Converter")
    st.markdown("Convert between different units of measurement with ease!")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Length", "Weight", "Temperature", "Volume"])
    
    with tab1:
        st.header("Length Converter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            length_value = st.number_input(
                "Enter length value:",
                min_value=0.0,
                value=1.0,
                step=0.1,
                format="%.6f",
                key="length_value"
            )
            
            length_units = list(converter.length_units.keys())
            length_options = [converter.format_unit_option(unit) for unit in length_units]
            
            length_option_to_unit = {converter.format_unit_option(unit): unit for unit in length_units}
            
            from_length_option = st.selectbox(
                "From:",
                length_options,
                index=2,
                key="from_length"
            )
            
            to_length_option = st.selectbox(
                "To:",
                length_options,
                index=4,
                key="to_length"
            )
            
            from_length = length_option_to_unit[from_length_option]
            to_length = length_option_to_unit[to_length_option]
        
        with col2:
            result = converter.convert(length_value, from_length, to_length, 'length')
            
            st.markdown("### Result")
            
            if length_value < 0.001 or length_value > 1000000:
                formatted_input = f"{length_value:.6e}"
            else:
                formatted_input = f"{length_value:.6f}"
            
            if result < 0.001 or result > 1000000:
                formatted_result = f"{result:.6e}"
            else:
                formatted_result = f"{result:.6f}"
            
            st.markdown(f"**{formatted_input} {converter.get_unit_name(from_length)}** = ")
            st.markdown(f"**{formatted_result} {converter.get_unit_name(to_length)}**")
            
            if length_value > 0:
                st.progress(min(1.0, result / (length_value * 10)))
    
    with tab2:
        st.header("Weight Converter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight_value = st.number_input(
                "Enter weight value:",
                min_value=0.0,
                value=1.0,
                step=0.1,
                format="%.6f",
                key="weight_value"
            )
            
            weight_units = list(converter.weight_units.keys())
            weight_options = [converter.format_unit_option(unit) for unit in weight_units]
            
            weight_option_to_unit = {converter.format_unit_option(unit): unit for unit in weight_units}
            
            from_weight_option = st.selectbox(
                "From:",
                weight_options,
                index=2,
                key="from_weight"
            )
            
            to_weight_option = st.selectbox(
                "To:",
                weight_options,
                index=4,
                key="to_weight"
            )
            
            from_weight = weight_option_to_unit[from_weight_option]
            to_weight = weight_option_to_unit[to_weight_option]
        
        with col2:
            result = converter.convert(weight_value, from_weight, to_weight, 'weight')
            
            st.markdown("### Result")
            
            if weight_value < 0.001 or weight_value > 1000000:
                formatted_input = f"{weight_value:.6e}"
            else:
                formatted_input = f"{weight_value:.6f}"
            
            if result < 0.001 or result > 1000000:
                formatted_result = f"{result:.6e}"
            else:
                formatted_result = f"{result:.6f}"
            
            st.markdown(f"**{formatted_input} {converter.get_unit_name(from_weight)}** = ")
            st.markdown(f"**{formatted_result} {converter.get_unit_name(to_weight)}**")
            
            if weight_value > 0:
                st.progress(min(1.0, result / (weight_value * 10)))
    
    with tab3:
        st.header("Temperature Converter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            temp_value = st.number_input(
                "Enter temperature value:",
                value=0.0,
                step=0.1,
                format="%.2f",
                key="temp_value"
            )
            
            temp_units = ['C', 'F', 'K']
            temp_options = [converter.format_unit_option(unit) for unit in temp_units]
            
            temp_option_to_unit = {converter.format_unit_option(unit): unit for unit in temp_units}
            
            from_temp_option = st.selectbox(
                "From:",
                temp_options,
                index=0,
                key="from_temp"
            )
            
            to_temp_option = st.selectbox(
                "To:",
                temp_options,
                index=1,
                key="to_temp"
            )
            
            from_temp = temp_option_to_unit[from_temp_option]
            to_temp = temp_option_to_unit[to_temp_option]
        
        with col2:
            result = converter.convert(temp_value, from_temp, to_temp, 'temperature')
            
            st.markdown("### Result")
            
            if from_temp == 'C':
                from_display = f"{temp_value:.2f} °C"
            elif from_temp == 'F':
                from_display = f"{temp_value:.2f} °F"
            else:
                from_display = f"{temp_value:.2f} K"
            
            if to_temp == 'C':
                to_display = f"{result:.2f} °C"
            elif to_temp == 'F':
                to_display = f"{result:.2f} °F"
            else:
                to_display = f"{result:.2f} K"
            
            st.markdown(f"**{from_display}** = ")
            st.markdown(f"**{to_display}**")
            
            if to_temp == 'C':
                temp_scale = min(100, max(0, (result + 20) / 120 * 100))
            elif to_temp == 'F':
                temp_scale = min(100, max(0, (result - 32) / 180 * 100))
            else:
                temp_scale = min(100, max(0, (result - 273.15) / 100 * 100))
            
            st.progress(temp_scale / 100)
    
    with tab4:
        st.header("Volume Converter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            volume_value = st.number_input(
                "Enter volume value:",
                min_value=0.0,
                value=1.0,
                step=0.1,
                format="%.6f",
                key="volume_value"
            )
            
            volume_units = list(converter.volume_units.keys())
            volume_options = [converter.format_unit_option(unit) for unit in volume_units]
            
            volume_option_to_unit = {converter.format_unit_option(unit): unit for unit in volume_units}
            
            from_volume_option = st.selectbox(
                "From:",
                volume_options,
                index=1, 
                key="from_volume"
            )
            
            to_volume_option = st.selectbox(
                "To:",
                volume_options,
                index=2, 
                key="to_volume"
            )
            
            from_volume = volume_option_to_unit[from_volume_option]
            to_volume = volume_option_to_unit[to_volume_option]
        
        with col2:
            result = converter.convert(volume_value, from_volume, to_volume, 'volume')
            
            st.markdown("### Result")
            
            if volume_value < 0.001 or volume_value > 1000000:
                formatted_input = f"{volume_value:.6e}"
            else:
                formatted_input = f"{volume_value:.6f}"
            
            if result < 0.001 or result > 1000000:
                formatted_result = f"{result:.6e}"
            else:
                formatted_result = f"{result:.6f}"
            
            st.markdown(f"**{formatted_input} {converter.get_unit_name(from_volume)}** = ")
            st.markdown(f"**{formatted_result} {converter.get_unit_name(to_volume)}**")
            
            if volume_value > 0:
                st.progress(min(1.0, result / (volume_value * 10)))
    
    st.markdown("---")
    st.markdown("### How to use this converter")
    st.markdown("""
    1. Select the measurement type tab (Length, Weight, Temperature, or Volume)
    2. Enter the value you want to convert
    3. Select the source unit from the "From" dropdown
    4. Select the target unit from the "To" dropdown
    5. The result will be displayed instantly
    """)
    
    with st.expander("About this app"):
        st.markdown("""
        This Unit Converter app allows you to convert between different units of measurement:
        
        - **Length**: millimeters, centimeters, meters, kilometers, inches, feet, yards, miles
        - **Weight**: milligrams, grams, kilograms, ounces, pounds, tons
        - **Temperature**: Celsius, Fahrenheit, Kelvin
        - **Volume**: milliliters, liters, gallons, quarts, pints, fluid ounces
        
        The app uses standard conversion factors and formulas to ensure accurate results.
        """)


if __name__ == "__main__":
    main()