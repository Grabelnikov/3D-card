# Control Panel Integration Guide

This guide explains how to integrate the modular control panel system into other prototypes and projects.

## Overview

The control panel has been separated into three reusable components:

- **`grid-system.css`** - Flexible grid layout system for panel positioning
- **`panel.css`** - Complete control panel styling and theming
- **`panel.html`** - Control panel HTML structure and controls

## Quick Start

### Basic Integration

1. **Copy the required files** to your project:
   ```
   your-project/
   ├── grid-system.css
   ├── panel.css
   └── panel.html (or copy content)
   ```

2. **Include CSS files** in your HTML head:
   ```html
   <head>
       <link rel="stylesheet" href="grid-system.css">
       <link rel="stylesheet" href="panel.css">
       <!-- Your other styles -->
   </head>
   ```

3. **Use the HTML structure**:
   ```html
   <body>
       <div class="app-container" data-panel-position="left">
           <!-- Copy content from panel.html here -->
           <div class="control-panel">
               <!-- All controls from panel.html -->
           </div>
           
           <div class="app-content">
               <!-- Your main application content -->
           </div>
       </div>
   </body>
   ```

## Configuration Options

### Panel Positioning

The grid system supports flexible panel positioning:

```html
<!-- Left panel (default) -->
<div class="app-container" data-panel-position="left">

<!-- Right panel -->
<div class="app-container" data-panel-position="right">
```

### Custom Panel Width

Override the default panel width using CSS custom properties:

```css
:root {
    --panel-width: 350px; /* Default: 300px */
}
```

### Panel Gap

Adjust spacing between panel and content:

```css
:root {
    --panel-gap: 20px; /* Default: 0px */
}
```

## Responsive Behavior

The system automatically adapts to different screen sizes:

- **Desktop** (>1024px): Full panel width (300px default)
- **Tablet** (769px-1024px): Smaller panel width (250px)
- **Mobile** (≤768px): Panel stacks on top, 100% width

## Theming

### Color Customization

Override control panel colors:

```css
:root {
    --controls-bg: #f0f0f0;           /* Panel background */
    --controls-accent: #007AFF;        /* Accent color */
    --controls-text: #555;            /* Text color */
    --controls-text-dark: #222;       /* Dark text */
    --controls-border: #ccc;          /* Border color */
}
```

### Spacing Customization

Adjust control spacing:

```css
:root {
    --controls-gap-xs: 8px;   /* Extra small spacing */
    --controls-gap-sm: 10px;  /* Small spacing */
    --controls-gap-md: 16px;  /* Medium spacing */
    --controls-gap-lg: 24px;  /* Large spacing */
    --controls-gap-xl: 32px;  /* Extra large spacing */
}
```

## JavaScript Integration

### Required Event Listeners

Your JavaScript must bind to these control IDs:

```javascript
// File upload
document.getElementById('imageUpload').addEventListener('change', handleImageUpload);
document.getElementById('resetImage').addEventListener('click', resetImage);

// Effects controls
document.getElementById('shineToggle').addEventListener('change', toggleShine);
document.getElementById('shineIntensity').addEventListener('input', updateShineIntensity);
document.getElementById('innerShadowLightOpacity').addEventListener('input', updateLightShadow);
document.getElementById('innerShadowDarkOpacity').addEventListener('input', updateDarkShadow);

// And all other controls...
```

### Value Display Updates

Update value display spans when controls change:

```javascript
function updateShineIntensity(event) {
    const value = event.target.value;
    document.getElementById('shineIntensityValue').textContent = value;
    // Apply the value to your application logic
}
```

### Control Pattern Helper

Use this pattern for all range controls:

```javascript
function attachSliderListener(controlId, settingName) {
    const slider = document.getElementById(controlId);
    const valueDisplay = document.getElementById(controlId + 'Value');
    
    slider.addEventListener('input', (event) => {
        const value = event.target.value;
        valueDisplay.textContent = value;
        // Update your settings object
        settings[settingName] = value;
        // Apply changes to your application
    });
}
```

## Advanced Usage

### Custom Controls

Add new controls following the existing pattern:

```html
<!-- In panel.html -->
<div class="control-group">
    <div class="heading">
        <label for="myNewControl">My Control</label>
        <span><span id="myNewControlValue">50</span>%</span>
    </div>
    <input type="range" id="myNewControl" min="0" max="100" value="50" step="1">
</div>
```

```javascript
// In your JavaScript
attachSliderListener('myNewControl', 'myNewSetting');
```

### Panel Sections

Organize controls into logical sections:

```html
<h4>My New Section</h4>
<div class="control-group">
    <!-- Your controls -->
</div>
```

### Conditional Controls

Hide/show controls based on application state:

```javascript
// Hide a control group
document.querySelector('.grain-control').style.display = 'none';

// Show a control group
document.querySelector('.grain-control').style.display = 'block';
```

## Examples

### Minimal Integration

For a simple project with just basic controls:

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="grid-system.css">
    <link rel="stylesheet" href="panel.css">
</head>
<body>
    <div class="app-container">
        <div class="control-panel">
            <h4>Controls</h4>
            <div class="control-group">
                <div class="heading">
                    <label for="opacity">Opacity</label>
                    <span><span id="opacityValue">100</span>%</span>
                </div>
                <input type="range" id="opacity" min="0" max="100" value="100">
            </div>
        </div>
        
        <div class="app-content">
            <h1>My Application</h1>
        </div>
    </div>
</body>
</html>
```

### Full Integration

For projects needing all controls, simply copy the complete `panel.html` content.

## Migration from Single File

If migrating from a single-file approach:

1. Remove inline panel styles from your HTML
2. Remove panel-related CSS custom properties from `:root`
3. Add the CSS file links
4. Your existing JavaScript should continue working unchanged

## Performance Notes

- CSS files are cacheable across projects
- Minimal overhead (~15KB total for both CSS files)
- No JavaScript dependencies
- Works with any framework or vanilla JS

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support  
- Safari: Full support
- IE11: Basic support (no CSS custom properties)

## Troubleshooting

### Controls Not Styling Correctly
- Ensure `panel.css` is loaded after `grid-system.css`
- Check that CSS custom properties are supported

### Layout Issues
- Verify the `app-container` structure is correct
- Check `data-panel-position` attribute
- Ensure both CSS files are loaded

### JavaScript Not Working
- Verify all control IDs match between HTML and JavaScript
- Check that value display spans follow the `controlId + 'Value'` pattern

## Contributing

When adding new controls:
1. Follow the existing HTML structure pattern
2. Use CSS custom properties for theming
3. Update this documentation with new controls
4. Test across all breakpoints