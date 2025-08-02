# TailwindCSS Component Showcase

A comprehensive Flask web application that showcases all TailwindCSS components and utilities in one beautiful, organized interface. Perfect for designers and developers who want to explore, customize, and theme TailwindCSS components.

## 🚀 Features

- **Complete Component Library**: Displays all major TailwindCSS components including:
  - Typography (headings, text styles, lists, blockquotes)
  - Buttons (primary, secondary, outline, states, with icons)
  - Forms (inputs, selects, textareas, validation states, switches)
  - Cards (basic, with images, pricing, stats, testimonials)
  - Navigation (horizontal/vertical nav, breadcrumbs, tabs, pagination, dropdowns)
  - Tables (basic, sortable, responsive, with actions)
  - Layout (grids, flexbox, containers, sidebars, card layouts)
  - Media (images, avatars, galleries, video players, icons)
  - Feedback (alerts, notifications, toasts, progress indicators)
  - Backgrounds & Effects (gradients, glassmorphism, shadows, patterns, overlays)
  - Badges & Labels (status badges, notification counts, tags, chips, category labels)
  - Progress & Loading (progress bars, spinners, skeleton loaders, step indicators)
  - Modals & Overlays (dialogs, confirmations, forms, tooltips, popovers)
  - Accordions & Collapsibles (FAQ sections, expandable content, card-based)
  - Utilities (spacing, colors, borders, shadows, positioning)

- **Multi-Page Application**: Clean navigation between main landing page and component showcase
- **Responsive Design**: All components are mobile-first and responsive
- **Dark Mode Support**: Toggle between light and dark themes with persistent preference
- **Interactive Components**: Working modals, accordions, dropdowns with JavaScript functionality
- **Modern Interface**: Minimalistic, sleek design with professional aesthetics
- **Organized Structure**: Components are logically grouped and easy to navigate navigate

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd gen-theme
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000` to view the showcase

## 📁 Project Structure

```
gen-theme/
├── app.py                          # Main Flask application with routes
├── requirements.txt                # Python dependencies
├── README.md                      # This file
├── CHANGELOG.md                   # Complete change history
├── LICENSE                        # License file
└── templates/
    ├── base.html                  # Base template with dark mode & enhanced footer
    ├── index.html                 # Minimalistic main landing page
    ├── showcase.html              # Complete component showcase page
    ├── coming_soon.html          # Template for disabled features
    └── components/
        ├── typography.html        # Typography examples
        ├── buttons.html          # Button components
        ├── forms.html            # Form elements & validation
        ├── cards.html            # Card components & layouts
        ├── navigation.html       # Navigation with dropdowns (z-index fixed)
        ├── tables.html           # Table examples & responsive design
        ├── layout.html           # Layout utilities (HTML structure fixed)
        ├── media.html            # Media components & galleries
        ├── feedback.html         # Feedback components & alerts
        ├── backgrounds.html      # Gradients, glassmorphism, effects
        ├── badges.html           # Status badges, tags, notification counts
        ├── progress.html         # Progress bars, loading states, spinners
        ├── modals.html           # Interactive modals, dialogs, overlays
        ├── accordions.html       # Collapsible content & FAQ sections
        └── utilities.html        # Utility classes & helpers
```

## 🌐 Application Routes

- `/` - Main landing page (minimalistic design)
- `/showcase` - Complete component showcase (15 sections)
- `/interactions` - Coming soon page for interactions & animations
- `/transitions` - Coming soon page for transitions & effects

## 🎨 Customization

### Theming
The application uses TailwindCSS CDN which can be easily customized. To modify the theme:

1. **Edit the TailwindCSS config** in `templates/base.html`:
   ```javascript
   tailwind.config = {
       theme: {
           extend: {
               colors: {
                   primary: '#your-color',
                   secondary: '#your-color',
               }
           }
       }
   }
   ```

2. **Add custom CSS** by including additional stylesheets in the base template

3. **Modify component styles** by editing the individual component templates

### Adding New Components
1. Create a new template file in `templates/components/`
2. Add the component showcase HTML with TailwindCSS classes
3. Include the component in `templates/index.html`
4. Update the navigation in `templates/base.html` if needed

### Dark Mode Support
The application includes a built-in dark mode toggle that:
- Automatically detects system preference on first visit
- Persists user preference in localStorage
- Smoothly transitions between light and dark themes
- Updates all components with appropriate dark mode styling

To customize dark mode colors, modify the dark mode classes in component templates or update the TailwindCSS configuration.

## 🔧 Development

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run in development mode
python app.py
```

The application will run on `http://localhost:5000` with debug mode enabled.

### File Structure for Components
Each component template should follow this structure:
```html
<!-- Component Examples -->
<div class="space-y-8">
    <!-- Component Category 1 -->
    <div class="bg-white p-6 rounded-lg shadow-sm border">
        <h3 class="text-lg font-semibold mb-4">Component Category Title</h3>
        <!-- Component examples here -->
    </div>
    
    <!-- More categories... -->
</div>
```

## 📱 Responsive Design

All components are built with mobile-first responsive design:
- **Mobile**: Base styles
- **Tablet**: `md:` prefix classes
- **Desktop**: `lg:` and `xl:` prefix classes

## 🎯 Use Cases

- **Design System Development**: Use as a starting point for your design system
- **Component Library**: Reference for TailwindCSS component implementations
- **Theming**: Experiment with different color schemes and styles
- **Learning**: Understand TailwindCSS class usage and patterns
- **Prototyping**: Quickly grab component code for prototypes

## 📄 Documentation

- **README.md** - Setup instructions and feature overview
- **CHANGELOG.md** - Complete change history and version tracking
- **LICENSE** - MIT License terms

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add new components or improve existing ones
4. Ensure responsive design and accessibility
5. Update CHANGELOG.md with your changes
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TailwindCSS](https://tailwindcss.com/) for the amazing utility-first CSS framework
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework
- [Font Awesome](https://fontawesome.com/) for the icon library

## 🔮 Recent Updates & Enhancements

- [x] **Dark mode toggle** - Complete implementation with localStorage persistence
- [x] **Multi-page structure** - Separate landing page and showcase
- [x] **Minimalistic design** - Clean, professional main page
- [x] **Enhanced footer** - Professional footer with links and social media
- [x] **Interactive components** - Working modals, accordions, dropdowns
- [x] **Comprehensive showcase** - 15 component categories
- [x] **Responsive design** - Mobile-first approach throughout
- [x] **Bug fixes** - HTML structure and z-index issues resolved

## 🔮 Future Enhancements

- [ ] Component code viewer with syntax highlighting
- [ ] Copy-to-clipboard functionality for component code
- [ ] Live theme editor with real-time preview
- [ ] Export functionality for custom themes
- [ ] Interactive component playground
- [ ] Search and filter components
- [ ] Component usage analytics
- [ ] API for programmatic access

---

**Start exploring TailwindCSS components now!** 🚀

