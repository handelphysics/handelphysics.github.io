# P.H. Handel Research Archive Website

## Overview

This website showcases the complete research archive of Professor Peter H. Handel, spanning 65 years (1958-2023) of groundbreaking contributions to quantum physics, semiconductor devices, atmospheric electricity, and fundamental noise theory.

## Website Structure

```
website/
├── index.html              # Main landing page with focus area cards
├── css/
│   └── styles.css         # Modern, responsive styling
├── quantum-1f-noise.html   # Quantum theory of 1/f noise papers
├── gan-devices.html        # GaN & wide-bandgap semiconductor papers
├── atmospheric-physics.html # Ball lightning & atmospheric electricity
├── sensors.html            # Precision sensors & MEMS resonators
├── oscillators.html        # Phase noise & frequency standards
└── nanotechnology.html     # Quantum nanotechnology & emerging devices
```

## Features

### Main Page (index.html)
- Six focus area cards with emoji icons
- Hover effects and modern card design
- Responsive grid layout
- Paper count badges for each area
- Professional color scheme (blue/navy palette)

### Focus Area Pages
Each page includes:
- Descriptive header explaining the research area
- Comprehensive list of relevant papers
- Paper metadata (number, title, authors, venue)
- Links to PDFs and summaries where available
- Back navigation to main page
- Highlight styling for landmark papers

### Styling
- Modern, clean design with card-based layouts
- Smooth hover animations and transitions
- Fully responsive (mobile, tablet, desktop)
- Professional color palette
- Accessible typography and contrast

## How to Use

### Viewing Locally

1. Open `website/index.html` in any modern web browser
2. Click on any focus area card to view papers in that category
3. Click paper links to access PDFs or summaries
4. Use the back button or navigation to return to main page

### Deploying to Web Server

Simply copy the entire `website/` directory to your web server. The site uses:
- Pure HTML5 and CSS3 (no build process needed)
- Relative links for portability
- No external dependencies

### Customization

**Colors:** Edit `css/styles.css` `:root` variables:
```css
--primary-color: #2c3e50;
--secondary-color: #3498db;
--accent-color: #e74c3c;
```

**Images:** Replace emoji placeholders in focus area cards with actual images:
```html
<div class="focus-image">
    <img src="images/quantum-noise.jpg" alt="Quantum Noise">
</div>
```

## Six Major Research Focus Areas

1. **Quantum Theory of 1/f Noise** (~65 papers)
   - Fundamental quantum mechanical foundations
   - Infrared divergences and bremsstrahlung
   - Universal explanation across physical systems

2. **GaN & Wide-Bandgap Semiconductors** (~17 papers)
   - Piezoelectric quantum noise in HEMTs
   - Reliability and stability diagnostics
   - RF power amplifiers and 5G applications

3. **Atmospheric Electricity & Ball Lightning** (~25 papers)
   - Maser-caviton theory
   - Polarization catastrophe mechanism
   - Thunderstorm electrification

4. **Precision Sensors & MEMS** (~28 papers)
   - Biochemical FET sensors
   - Piezoelectric resonators
   - Quantum detection limits

5. **Phase Noise & Frequency Standards** (~22 papers)
   - Oscillator phase noise theory
   - Quartz crystal resonators
   - Ultra-stable frequency references

6. **Quantum Nanotechnology** (~15 papers)
   - Quantum proximity effects
   - Decoherence in nanodevices
   - Fundamental scaling limits

## Technical Notes

- All links to PDFs use relative paths from Papers/ directory
- Summary files are accessed via relative links
- External DOI links open in new tabs
- CSS uses modern features (Grid, Flexbox, CSS Variables)
- Optimized for print media (clean printouts)
- Semantic HTML5 markup throughout

## Browser Compatibility

Tested and compatible with:
- Chrome/Edge (v90+)
- Firefox (v88+)
- Safari (v14+)
- Mobile browsers (iOS Safari, Chrome Android)

## Credits

**Research:** Prof. Peter H. Handel (www.umsl.edu/~handel)
**Institution:** University of Missouri - St. Louis
**Website Design:** 2024
**Archive:** 317 publications (1958-2023)

## Contact

For inquiries about the research archive:
- Email: handel@umsl.edu
- Web: http://www.umsl.edu/~handel
