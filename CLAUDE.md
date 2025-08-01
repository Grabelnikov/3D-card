# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 3D Card Prototype - AI Assistant Guidelines

## 🚀 Quick Reference

### Essential Commands
```bash
npm start              # Development server (http://127.0.0.1:8080)
npm test              # Basic validation
```

### Key Files & Classes
- **`index.html`** - Main application (HTML + JS, now uses external CSS)
- **`grid-system.css`** - Portable grid layout system for panel positioning
- **`panel.css`** - Complete control panel styling and theming
- **`panel.html`** - Control panel HTML structure (copy content for integration)
- **`GrainShadowRenderer`** (line ~572) - WebGL shadow effects
- **`SimpleCardSystem`** (line ~1033) - Main controller  
- **`assets/sofa.jpg`** - Default background image

### Control Pattern (Add New Features)
```javascript
// 1. Add to settings
this.settings = { newParameter: defaultValue };
// 2. Create UI control
attachSliderListener('newParameter', 'newParameter');
// 3. Apply effect
element.style.property = this.settings.newParameter;
```

---

## 📋 Planning & Todo Management

### Planning Workflow
1. **Always enter plan mode first** for non-trivial tasks
2. **Write detailed plans** to `.claude/tasks/TASK_NAME.md` 
3. **Plan should include**: implementation steps, reasoning, task breakdown
4. **Think MVP** - don't over-plan
5. **Get approval** before proceeding - ask user to review plan
6. **Update plans** as you work with implementation details

### Todo Management Strategy
- **Use TodoWrite tool** for active task tracking during implementation
- **Use .claude/tasks/*.md files** for planning and detailed documentation
- **Mark tasks complete immediately** when finished - don't batch
- **Only one task "in_progress"** at a time
- **Break complex tasks** into specific, actionable steps

### When to Use Which Tool
- **TodoWrite**: Active implementation tracking, real-time progress
- **Task files**: Planning, detailed specs, handoff documentation
- **Both**: For complex features requiring both planning and tracking

---

## 🛠️ Tool Usage Patterns

### Investigation & Search
```javascript
// For finding specific code/functions
Glob + Grep (parallel)      // Multiple searches simultaneously
Read                        // Specific files you know exist

// For open-ended research
Task tool                   // Complex investigations, multiple rounds
```

### Code Modification Priority
1. **Edit/MultiEdit** - Modify existing files (preferred)
2. **Write** - Only when creating new files is absolutely necessary
3. **Never create** documentation files unless explicitly requested

### Performance-Critical Paths
- **Always test immediately** after changes affecting animations
- **Check server availability** (developer usually runs `npm start` in separate terminal)
- **Verify 60fps performance** in browser at http://127.0.0.1:8080
- **Check all controls** work after modifications

---

## 🎯 Decision Making Framework

### When Requirements Are Unclear
1. **Analyze existing patterns** in the codebase first
2. **Choose the approach** that matches current architecture
3. **Prefer simpler implementation** (MVP mindset)
4. **Ask for clarification** only when multiple valid approaches exist
5. **Flag potential performance impacts** immediately

### Priority System
- **60fps performance** - Non-negotiable
- **Real-time controls** - Must work instantly  
- **Single-file architecture** - Maintain unless complexity demands otherwise
- **Designer accessibility** - Code must be understandable

### Conflict Resolution
- **Performance vs Features**: Always choose performance
- **Simplicity vs Flexibility**: Choose simplicity for MVP
- **Current vs Future**: Implement current needs, document future plans

---

## 🔧 Error Handling & Debugging

### Common Issues & Solutions
```javascript
// Performance degradation
- Check will-change usage (use sparingly)
- Verify requestAnimationFrame usage
- Test with all effects enabled

// Control not working
- Verify attachSliderListener() call
- Check settings object has property
- Ensure CSS custom property is applied

// Animation jank
- Use CSS transforms instead of position changes
- Batch DOM updates
- Cache calculations outside event handlers
```

### Performance Testing
```bash
# Run server and test in Chrome DevTools
npm start
# Check Performance tab for 60fps
# Monitor Memory tab for leaks
# Test with all controls at maximum values
```

### WebGL Issues
- Check browser WebGL support
- Verify shader compilation
- Test canvas context creation
- Monitor console for WebGL errors

---

## 🔍 Research Patterns

### Understanding Existing Code
1. **Start with architecture overview** (lines 326-383 in this file)
2. **Read main classes** (GrainShadowRenderer, SimpleCardSystem)
3. **Trace control flow** from UI controls to visual effects
4. **Check CSS custom properties** usage pattern

### Adding New Features
1. **Find similar existing feature** for pattern reference
2. **Identify required settings** for controls
3. **Determine CSS/JS integration points**
4. **Plan WebGL requirements** if needed

### External Knowledge Requirements
- **Use Task tool** for researching libraries, techniques, best practices
- **Check for existing solutions** in the codebase first
- **Prefer vanilla JS solutions** over adding dependencies

---

## 📊 Project Overview

**Interactive 3D card prototype** demonstrating celebratory moment UI for Airbnb. Features smooth animations, dynamic shadows with natural color bleeding, and real-time parameter controls. Built as proof-of-concept to get design team buy-in and help developers evaluate implementation feasibility.

### Target Users
1. **Airbnb Design Team**: Evaluate visual impact and interaction feel
2. **Airbnb Developers**: Assess technical feasibility and implementation complexity

### Success Metrics
- Designers can tweak all visual parameters in real-time during presentations
- Interaction runs at 60fps on Chrome desktop
- Developers can understand implementation approach within 5 minutes
- Zero dependencies for maximum portability
- Deployable to Vercel in under 2 minutes

### Technical Stack
- **Frontend**: Vanilla HTML/CSS/JavaScript (no frameworks unless absolutely necessary)
- **Graphics**: WebGL for advanced shadow effects only
- **Styling**: Inline CSS for dynamic properties, CSS variables for theming
- **Deployment**: Static hosting on Vercel
- **Target**: Chrome desktop (primary), mobile-friendly bonus

---

## ✅ Current Implementation Status

### ✅ Implemented Features
- ✅ **3D Card System**: Mouse-controlled rotation with smooth animations
- ✅ **Duplicate Shadow Layer**: Blurred copy for natural color bleeding
- ✅ **Dynamic Controls**: Real-time parameter adjustment sidebar
- ✅ **Background Parallax**: Smart sizing with overflow handling
- ✅ **WebGL Grain Shadows**: Fragment shader-based grain effects
- ✅ **Performance Optimizations**: 60fps animations with requestAnimationFrame

### ✅ Current Controls Available
- Duplicate card scale, opacity, Y offset, blur
- Rotating shadows toggle
- Interactive motion toggle  
- Dynamic shine effect toggle
- Manual rotation controls (X/Y axes)
- Background parallax toggle and intensity control
- Grain shadow controls (scale, intensity, bias)

### 🏗️ Architecture Patterns in Use

#### Settings Management
```javascript
// Centralized settings object pattern
this.settings = {
    duplicateScale: 1.05,
    duplicateOpacity: 0.7,
    parallaxEnabled: true,
    grainScale: 0.025,
    // ... other parameters
};
```

#### CSS Transform System
- Transform order: `rotateX() rotateY() translateZ() [scale()] [translate()]`
- CSS custom properties: `--rot-x`, `--rot-y`, `--dup-transform`
- Layered shadows: 6px, 18px, 36px offsets

#### Control Binding Pattern
```javascript
attachSliderListener('controlId', 'settingName');
```

---

## 🚧 Planned Features (Future Implementation)

### 1. Image Upload (Priority: High)
**Implementation**: Local file upload with instant preview
- Accept: PNG, JPG only (max 5MB, 2000×2000)
- Replace gradient on both main and duplicate cards
- Add reset to default option

### 2. Advanced Animation Controls (Priority: Medium)
- Color bleeding intensity controls
- Animation timing curve adjustments
- Z-depth fine-tuning
- Celebration animation triggers

### 3. Multiple Card Support (Priority: Low)
- Support for multiple cards in scene
- Card-to-card interactions
- Batch control applications

---

## 🎨 Design Guidelines

### Visual Standards
- **Apple TV OS inspiration**: Depth, smooth transitions, elegant hover states
- **Color bleeding**: Enhance, don't distract
- **Shadow accuracy**: Must feel physically accurate
- **Control intuitiveness**: Non-technical users should understand

### Animation Requirements
- **60fps mandatory** with all effects enabled
- **Smooth transitions** on rapid mouse movement
- **No jank** on parameter changes
- **Mouse leave easing**: 0.6s cubic-bezier

### Code Quality
- **Descriptive variables** that designers understand
- **Comment complex calculations** (especially 3D transforms)  
- **Organized control panel** by visual effect type
- **Visual clarity** - code readable by designers

---

## 🧪 Testing & Validation

### Actionable Testing Checklist
```bash
# 1. Performance Test (assumes server running at http://127.0.0.1:8080)
# Open Chrome DevTools > Performance tab
# Record 10 seconds of interaction  
# Verify consistent 60fps

# 2. Control Test  
# Move every slider/toggle and verify instant feedback
# Test rapid parameter changes for smoothness
# Verify no console errors

# 3. Edge Case Test
# Test fullscreen and windowed modes
# Test with/without WebGL support
# Test on different screen sizes

# 4. Feature Integration Test
# Enable all effects simultaneously
# Verify performance doesn't degrade
# Test control combinations
```

### Performance Benchmarks
- **Frame rate**: Consistent 60fps during interaction
- **Memory usage**: No leaks during extended use
- **Load time**: Under 2 seconds on desktop
- **Control response**: Under 16ms (1 frame) latency

---

## 🚀 Deployment & Development

### Development Server
```bash
npm start                    # Recommended (http://127.0.0.1:8080)
npx http-server             # Alternative (http://localhost:8080)
```

**Note**: Developer typically runs server in separate terminal. Claude should check if server is accessible at http://127.0.0.1:8080 before attempting to launch new instances.

### Deploy to Vercel
```bash
# CLI method
npm i -g vercel
vercel --prod

# Or drag project folder to vercel.com dashboard
```

### File Structure
```
/
├── index.html          # Single-file application (HTML + CSS + JS)
├── assets/sofa.jpg     # Default card background image  
└── package.json        # Dev dependencies (live-server)
```

---

## 🎯 AI Assistant Instructions

### Code Modification Priorities
1. **Preserve all existing functionality** unless explicitly asked to remove
2. **Maintain single-file architecture** unless complexity demands separation
3. **Test performance impact** of new features immediately
4. **Add controls to sidebar** following existing patterns
5. **Document non-obvious calculations**

### Communication Style
- **Visual/UX changes**: Explain in designer-friendly terms
- **Technical details**: Provide for developer audience  
- **Performance concerns**: Flag immediately
- **Alternatives**: Suggest when requests might impact smoothness

### Quality Gates
- ✅ **All controls provide instant visual feedback**
- ✅ **Smooth transitions on rapid mouse movement**
- ✅ **No jank on parameter changes**
- ✅ **Works fullscreen and windowed**
- ✅ **Graceful degradation if features unsupported**

---

## 🔄 Implementation Workflow

### For New Features
1. **Research existing patterns** in codebase
2. **Plan implementation** with TodoWrite
3. **Start with simplest version**
4. **Add controls** only if designers need them
5. **Test performance immediately**
6. **Document approach** for future reference

### For Bug Fixes
1. **Reproduce issue** with specific steps
2. **Identify root cause** in code
3. **Test fix** doesn't break other features
4. **Verify performance** remains at 60fps
5. **Update relevant documentation**

### For Performance Optimization
1. **Profile current performance** with DevTools
2. **Identify bottlenecks** systematically
3. **Apply optimizations** incrementally
4. **Measure improvement** after each change
5. **Ensure no feature regression**