# Research Insights Frontend

React-based frontend application with accessibility-first design.

## Quick Start

```bash
npm install
npm start
```

Opens at `http://localhost:3000`

## Available Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App (irreversible)

## Project Structure

```
src/
├── components/          # React components
│   ├── SearchBar.js    # Search input with ARIA labels
│   ├── FilterGroup.js  # Accessible radio button groups
│   ├── ProblemList.js  # List of identified issues
│   └── ProblemItem.js  # Individual issue cards
├── services/
│   └── api.js          # API service layer
├── styles/             # CSS with WCAG compliance
│   ├── index.css       # Global styles and tokens
│   ├── App.css         # Main app layout
│   ├── SearchBar.css
│   ├── FilterGroup.css
│   ├── ProblemList.css
│   └── ProblemItem.css
├── App.js              # Main application component
└── index.js            # Entry point
```

## Component Overview

### App.js
Main application component managing state and API calls.

**State:**
- `problems` - Array of identified challenges
- `loading` - Loading state
- `selectedGroup` - Current user group filter
- `selectedCategory` - Current category filter

### SearchBar.js
Accessible search form with:
- Proper label association
- Required field indicators
- Help text with `aria-describedby`
- Keyboard support

### FilterGroup.js
Radio button group component featuring:
- `<fieldset>` and `<legend>` structure
- Custom styled radio buttons
- Keyboard navigation (arrow keys)
- Clear focus indicators

### ProblemList.js
Semantic list container with:
- `role="list"` for screen readers
- Empty state handling
- Responsive layout

### ProblemItem.js
Individual challenge card with:
- Severity indicators
- Expandable descriptions
- ARIA attributes for state
- High contrast design

## Styling

### CSS Variables

All styles use CSS custom properties for consistency:

```css
--color-primary: #1a1a2e;
--color-accent: #1e5a8e;
--space-md: 1rem;
--font-size-base: 1rem;
```

### Responsive Design

Mobile-first approach with breakpoints:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

### Accessibility Features

- **Focus Indicators**: 2px outline on all interactive elements
- **Color Contrast**: All combinations meet WCAG AA (4.5:1+)
- **Font Scaling**: Supports 200% zoom
- **Keyboard Navigation**: Full support without mouse
- **Screen Reader**: ARIA labels and semantic HTML

## API Integration

The frontend communicates with the Flask backend via:

```javascript
import { analyzeText, getGroups, getCategories } from './services/api';

// Analyze research text
const result = await analyzeText(text, group, category);

// Get filter options
const groups = await getGroups();
const categories = await getCategories();
```

### Proxy Configuration

In development, API requests are proxied to avoid CORS issues:

```json
{
  "proxy": "http://localhost:5000"
}
```

For production, set `REACT_APP_API_URL` environment variable.

## Accessibility Testing

### Manual Testing

1. **Keyboard only**: Navigate without mouse
2. **Screen reader**: Test with NVDA or VoiceOver
3. **Zoom**: Test at 200% browser zoom
4. **Color blindness**: Use browser simulation tools

### Automated Testing

```bash
# Install Lighthouse
npm install -g lighthouse

# Run accessibility audit
lighthouse http://localhost:3000 --only-categories=accessibility
```

### Browser Extensions

- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE](https://wave.webaim.org/extension/)

## Building for Production

```bash
npm run build
```

Creates optimized production build in `build/` directory.

### Deployment

The build folder can be served by any static hosting service:

- **Vercel**: `vercel deploy`
- **Netlify**: Drag and drop `build/` folder
- **GitHub Pages**: Use `gh-pages` package
- **AWS S3**: Upload to S3 bucket with static hosting

### Environment Variables

For production, set:

```bash
REACT_APP_API_URL=https://your-api-domain.com
```

## Browser Support

- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

## Learn More

- [React Documentation](https://reactjs.org/)
- [Create React App](https://create-react-app.dev/)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Practices](https://www.w3.org/WAI/ARIA/apg/)
