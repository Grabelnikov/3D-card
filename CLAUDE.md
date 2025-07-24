# 3D Card Prototype - Project Guidelines for Claude

## Project Overview
Interactive 3D card prototype demonstrating celebratory moment UI for Airbnb. Features smooth animations, dynamic shadows with natural color bleeding, and real-time parameter controls. Built as proof-of-concept to get design team buy-in and help developers evaluate implementation feasibility.

## Target Users
1. **Airbnb Design Team**: Need to evaluate visual impact and interaction feel for celebratory moments
2. **Airbnb Developers**: Need to assess technical feasibility and implementation complexity

## Success Metrics
- Designers can tweak all visual parameters in real-time during presentations
- Interaction runs at 60fps on Chrome desktop
- Developers can understand implementation approach within 5 minutes
- Zero dependencies for maximum portability
- Deployable to Vercel in under 2 minutes

## Technical Stack
- **Frontend**: Vanilla HTML/CSS/JavaScript (no frameworks unless absolutely necessary)
- **Graphics**: WebGL for advanced shadow effects only
- **Styling**: Inline CSS for dynamic properties, CSS variables for theming
- **Deployment**: Static hosting on Vercel
- **Target**: Chrome desktop (primary), mobile-friendly bonus

## Inspiration & References
- **Apple TV OS cards**: Depth, smooth transitions, elegant hover states
- **Key differentiator**: Natural color bleeding via duplicate shadow layer

## Architecture Principles
- Single file simplicity - everything in one HTML unless it grows too complex
- Performance first - every animation must hit 60fps
- Real-time controls - all parameters adjustable without code changes
- Visual clarity - code should be understandable by designers

## Coding Standards
- Use descriptive variable names that designers understand
- Comment complex calculations (especially 3D transforms)
- Keep control panel organized by visual effect type
- CSS transforms in consistent order: `rotateX() rotateY() translateZ() [scale()] [translate()]`
- Use requestAnimationFrame for smooth animations
- Debounce/throttle mouse events if performance drops

## Key Features & Controls
### Current Controls
- Duplicate card scale, opacity, Y offset, blur
- Rotating shadows toggle
- Interactive motion toggle
- Dynamic shine effect toggle
- Manual rotation controls (X/Y axes)
- Background parallax toggle and intensity control
- Smart background sizing (cover vs parallax overflow)

### Future Control Considerations
- Color bleeding intensity
- Animation timing curves
- Z-depth adjustments
- Multiple card support
- Celebration animation triggers

## Common Patterns
### Adding New Controls
```javascript
// 1. Add to settings object
this.settings = {
    newParameter: defaultValue
};

// 2. Create control UI
attachSliderListener('newParameter', 'newParameter');

// 3. Apply in transform/effect methods
element.style.property = this.settings.newParameter;
```

### Performance Optimization
- Use CSS transforms over position changes
- Batch DOM updates
- Cache calculations outside event handlers
- Use CSS will-change sparingly

## Constraints & Edge Cases
- Must maintain 60fps with all effects enabled
- Shadow calculations must feel physically accurate
- Color bleeding should enhance, not distract
- Controls must be intuitive for non-technical users
- Mouse leave animations need special easing (0.6s cubic-bezier)

## Testing Checklist
- [ ] All controls provide instant visual feedback
- [ ] Smooth transitions on rapid mouse movement
- [ ] No jank on parameter changes
- [ ] Works fullscreen and windowed
- [ ] Graceful degradation if features unsupported

## AI Instructions
### When modifying this prototype:
1. Preserve all existing functionality unless explicitly asked to remove
2. Maintain single-file architecture unless complexity demands separation
3. Test performance impact of new features immediately
4. Add new controls to sidebar following existing patterns
5. Document any non-obvious calculations

### When adding features:
1. Start with simplest implementation
2. Add to controls panel only if designers need to adjust it
3. Ensure mobile compatibility isn't broken
4. Keep celebratory moment use case in mind

### Communication style:
- Explain visual/UX changes in designer-friendly terms
- Provide technical details for developer audience
- Flag any performance concerns immediately
- Suggest alternatives if request might impact smoothness

## Deployment Instructions

### Local Testing
```bash
# Option 1: Python (if installed)
python -m http.server 8000
# Visit http://localhost:8000

# Option 2: Node.js (if installed)
npx http-server
# Visit http://localhost:8080

# Option 3: VS Code
# Install "Live Server" extension
# Right-click index.html → "Open with Live Server"
```

### Deploy to Vercel
```bash
# Option 1: Vercel CLI
npm i -g vercel  # Install once
vercel          # Deploy (follow prompts)
vercel --prod   # Deploy to production

# Option 2: Drag & Drop
# Visit vercel.com
# Drag your project folder to the dashboard

# Option 3: Git Integration
# Push to GitHub/GitLab/Bitbucket
# Connect repo in Vercel dashboard
# Auto-deploys on every push
```

### Sharing Links
- Local: `http://localhost:8000`
- Vercel Preview: `https://[project-name]-[hash].vercel.app`
- Vercel Production: `https://[project-name].vercel.app`

## Planned Features

### 1. Grainy Shadow Effect (Priority: High)
**Implementation**: WebGL shader for rotating shadow only
- Use fragment shader similar to reference code
- Add controls: grain scale, intensity, bias
- No animation (static grain pattern)
- Performance impact acceptable if needed
- Must be toggleable for A/B comparison

**Controls to add:**
```javascript
grainScale: 0.025      // Size of grain pattern
grainIntensity: 1.5    // Strength of effect
grainBias: -0.5        // Light vs dark grain balance
grainEnabled: true     // Toggle for performance testing
```

**Reference Implementation Pattern:**
```glsl
// Simplified fragment shader approach from reference
// Apply simplex noise to shadow areas only
float simplexNoise(vec2 p) {
    // 2D simplex noise implementation
}

// Shadow with grain
if (shadow > 0.0) {
    vec2 noiseCoord = fragCoord / 100.0;
    float noiseValue = simplexNoise(noiseCoord * frequency);
    float grainVariation = (noiseValue - 0.5) * 2.0;
    shadow *= (1.0 + grainVariation * shadow);
}
```

**Key Implementation Notes:**
- Shadow layers use box-shadow offsets: 6px, 18px, 36px
- Grain modulates shadow intensity, not position
- Use WebGL canvas overlay for shadow rendering
- Composite with CSS elements using blend modes

### 2. Image Upload (Priority: Medium)
**Implementation**: Local file upload with instant preview
- Accept: PNG, JPG only
- Max size: 5MB
- Max resolution: 2000×2000
- Image persists until manual reset (no auto-clearing)
- Replace gradient on both main card and duplicate
- Blur on duplicate creates natural color bleed

**Technical approach:**
```javascript
// File input handler
const reader = new FileReader();
reader.onload = (e) => {
    mainCard.style.background = `url(${e.target.result})`;
    duplicateCard.style.background = `url(${e.target.result})`;
};
```

### 3. Background Parallax (Priority: Completed)
**Implementation**: CSS background-position manipulation with intelligent image sizing
- Dynamic background positioning based on card tilt direction
- Smart background sizing: cover (parallax off) vs calculated overflow (parallax on)
- Automatic aspect ratio handling for any image size
- Performance optimization through conditional sizing
- Smooth transitions matching existing card animations

**Controls added:**
```javascript
parallaxEnabled: true,     // Toggle parallax effect
parallaxIntensity: 2      // 0-10% shift at max tilt (default 2%)
```

**Core Algorithm:**
```javascript
// Dynamic background sizing for parallax overflow
calculateParallaxBackgroundSize(imageW, imageH) {
    const containerW = this.cardSystem.mainImage.offsetWidth;
    const containerH = this.cardSystem.mainImage.offsetHeight;
    
    // Calculate scale factor (same as background-size: cover)
    const scaleX = containerW / imageW;
    const scaleY = containerH / imageH;
    const coverScale = Math.max(scaleX, scaleY);
    
    // Apply cover scale + 15% overflow for parallax
    const finalScale = coverScale * 1.15;
    
    return `${Math.round(imageW * finalScale)}px ${Math.round(imageH * finalScale)}px`;
}

// Parallax positioning
const bgX = 50 - (rotY / maxTiltY) * parallaxIntensity;
const bgY = 50 + (rotX / maxTiltX) * parallaxIntensity;
```

**Key Implementation Notes:**
- Background moves opposite to card tilt for natural depth perception
- 15% overflow ensures movement range without revealing edges
- Conditional sizing: cover (off) vs calculated (on) for optimal performance
- Integrates seamlessly with existing mouse movement system
- Works with default sofa.jpg and uploaded images
- Rotation range limited to 0-20° for realistic interaction

## Implementation Guidelines

### For Grainy Shadow:
1. Create separate WebGL context for shadow rendering
2. Composite with existing CSS/DOM elements
3. Ensure shadow grain follows card rotation
4. Keep grain subtle for professional appearance
5. Test performance with all effects combined

### For Background Parallax (Completed):
1. Add parallax controls to sidebar following existing patterns
2. Implement conditional background sizing for performance
3. Ensure smooth integration with existing mouse movement
4. Test with various image aspect ratios
5. Validate 60fps performance with all effects enabled

### For Image Upload:
1. Add file input to control panel
2. Validate file type and size client-side
3. Use object-fit: cover for consistent sizing
4. Show upload progress/status
5. Add "reset to gradient" option

## Updated Constraints
- WebGL usage allowed specifically for shadow effects
- Maintain 60fps target but acceptable degradation with grain
- File handling must be memory efficient
- All new features must be toggleable

## Next Steps & Roadmap
1. ~~Implement background parallax~~ ✅ **COMPLETED**
2. Implement grainy shadow with WebGL
3. Add image upload functionality

### Reference Files
- `reference/grainy-shadow-reference.html` - Full WebGL grainy shadow implementation