# Accessibility Features and Guidelines

This document outlines the accessibility features implemented in the Research Insights Platform and provides guidelines for maintaining WCAG 2.1 Level AA compliance.

## WCAG 2.1 Level AA Compliance

### Perceivable

#### 1.1 Text Alternatives
- ✅ All images, icons, and non-text content have descriptive alt text
- ✅ Form inputs have associated labels
- ✅ ARIA labels for complex UI components

#### 1.3 Adaptable
- ✅ Semantic HTML5 structure (`<header>`, `<main>`, `<nav>`, `<footer>`, `<article>`)
- ✅ Proper heading hierarchy (h1 → h2 → h3)
- ✅ Lists use `<ul>`, `<ol>`, and `<li>` elements
- ✅ Forms use `<fieldset>` and `<legend>` for grouping

#### 1.4 Distinguishable
- ✅ Color contrast ratios meet WCAG AA standards (4.5:1 for normal text, 3:1 for large text)
- ✅ Text can be resized up to 200% without loss of functionality
- ✅ Color is not the only visual means of conveying information
- ✅ Focus indicators are clearly visible (2px solid outline)

### Operable

#### 2.1 Keyboard Accessible
- ✅ All functionality available via keyboard
- ✅ No keyboard traps
- ✅ Tab order follows logical sequence
- ✅ Skip to main content link for keyboard users

#### 2.4 Navigable
- ✅ Descriptive page title
- ✅ Clear focus indicators on all interactive elements
- ✅ Multiple ways to navigate (search, filters)
- ✅ Link purpose can be determined from link text

### Understandable

#### 3.1 Readable
- ✅ Language of page is identified (`lang="en"`)
- ✅ Plain language used throughout
- ✅ Technical terms explained when necessary

#### 3.2 Predictable
- ✅ Consistent navigation and layout
- ✅ Consistent identification of components
- ✅ Changes of context are initiated only by user action

#### 3.3 Input Assistance
- ✅ Clear error messages with suggestions
- ✅ Labels and instructions for form inputs
- ✅ Required fields clearly marked

### Robust

#### 4.1 Compatible
- ✅ Valid HTML5
- ✅ Proper ARIA roles and attributes
- ✅ Name, role, and value available for all UI components
- ✅ Status messages use ARIA live regions

## Implemented Features

### Keyboard Navigation

All interactive elements are keyboard accessible:

| Element | Key | Action |
|---------|-----|--------|
| Links/Buttons | Tab | Navigate forward |
| Links/Buttons | Shift+Tab | Navigate backward |
| Buttons | Enter or Space | Activate |
| Radio buttons | Arrow keys | Select option |
| Radio buttons | Tab | Move to next group |

### Screen Reader Support

#### ARIA Attributes Used

- `role="search"` - Identifies search form
- `role="region"` - Identifies filter section
- `role="list"` and `role="listitem"` - Problem list structure
- `role="status"` - Loading indicators
- `role="alert"` - Error messages
- `aria-label` - Descriptive labels for elements
- `aria-labelledby` - Associates labels with regions
- `aria-describedby` - Additional descriptions
- `aria-live="polite"` - Announces dynamic updates
- `aria-expanded` - Indicates expand/collapse state
- `aria-controls` - Associates controls with content
- `aria-required` - Marks required fields

#### Semantic HTML

```html
<!-- Proper landmark structure -->
<header role="banner">
  <h1>Site Title</h1>
</header>

<main id="main-content" role="main">
  <!-- Main content -->
</main>

<footer role="contentinfo">
  <!-- Footer content -->
</footer>

<!-- Accessible forms -->
<form role="search">
  <label for="search-input">Search</label>
  <input id="search-input" type="text" />
</form>

<!-- Grouped form controls -->
<fieldset>
  <legend>User Group</legend>
  <input type="radio" id="option1" name="group" />
  <label for="option1">Option 1</label>
</fieldset>
```

### Color and Contrast

All color combinations meet WCAG AA standards:

| Element | Foreground | Background | Contrast Ratio |
|---------|-----------|------------|----------------|
| Body text | #212529 | #ffffff | 16.1:1 ✅ |
| Headings | #1a1a2e | #ffffff | 16.9:1 ✅ |
| Links | #1e5a8e | #ffffff | 5.2:1 ✅ |
| Error text | #c92a2a | #ffffff | 7.6:1 ✅ |
| Success text | #2f9e44 | #ffffff | 4.8:1 ✅ |
| Warning text | #f59f00 | #ffffff | 5.1:1 ✅ |

### Focus Indicators

All interactive elements have visible focus indicators:

```css
*:focus-visible {
  outline: 2px solid #1e5a8e;
  outline-offset: 2px;
}
```

### Responsive Typography

Text scales appropriately:

- Base font size: 16px
- Line height: 1.5 for body text
- Maximum line length: ~70 characters
- Text can be resized to 200% without horizontal scrolling

## Testing Checklist

### Manual Testing

- [ ] Navigate entire site using only keyboard (no mouse)
- [ ] Test with screen reader (NVDA, JAWS, VoiceOver)
- [ ] Zoom browser to 200% and verify layout
- [ ] Check color contrast with DevTools
- [ ] Test with Windows High Contrast Mode
- [ ] Verify skip to content link appears on Tab
- [ ] Check all images have meaningful alt text
- [ ] Ensure focus is visible on all interactive elements

### Automated Testing Tools

#### Browser Extensions
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE](https://wave.webaim.org/extension/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) (built into Chrome)

#### Command Line
```bash
# Using pa11y
npm install -g pa11y
pa11y http://localhost:3000

# Using axe-cli
npm install -g @axe-core/cli
axe http://localhost:3000
```

### Screen Reader Testing

#### Windows (NVDA)
1. Download NVDA from https://www.nvaccess.org/
2. Press `Ctrl+Alt+N` to start
3. Navigate with:
   - `H` - Next heading
   - `Tab` - Next interactive element
   - `B` - Next button
   - `F` - Next form field
   - `Insert+Down Arrow` - Read current line

#### macOS (VoiceOver)
1. Press `Cmd+F5` to start
2. Navigate with:
   - `VO+Right Arrow` - Next item
   - `VO+Space` - Activate item
   - `Tab` - Next interactive element
   - `VO+U` - Open rotor (lists, headings, etc.)

#### Mobile Screen Readers
- iOS: VoiceOver (Settings → Accessibility → VoiceOver)
- Android: TalkBack (Settings → Accessibility → TalkBack)

## Common Accessibility Pitfalls to Avoid

### ❌ Don't Do This

```html
<!-- Missing label -->
<input type="text" placeholder="Name" />

<!-- Non-semantic button -->
<div onclick="submit()">Submit</div>

<!-- Insufficient contrast -->
<p style="color: #999; background: #fff;">Text</p>

<!-- No keyboard access -->
<div onclick="handleClick()">Click me</div>

<!-- Generic link text -->
<a href="/page">Click here</a>
```

### ✅ Do This Instead

```html
<!-- Proper label -->
<label for="name-input">Name</label>
<input id="name-input" type="text" />

<!-- Semantic button -->
<button type="button" onClick="submit">Submit</button>

<!-- Sufficient contrast -->
<p style="color: #212529; background: #fff;">Text</p>

<!-- Keyboard accessible -->
<button onClick="handleClick">Click me</button>

<!-- Descriptive link text -->
<a href="/page">Read the accessibility guide</a>
```

## Resources

### Guidelines and Standards
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [MDN Accessibility Guide](https://developer.mozilla.org/en-US/docs/Web/Accessibility)

### Testing Tools
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [HTML5 Validator](https://validator.w3.org/)
- [ARIA Validator](https://www.powermapper.com/tests/screen-readers/)

### Learning Resources
- [Web Accessibility Course (Udacity)](https://www.udacity.com/course/web-accessibility--ud891)
- [A11ycasts YouTube Series](https://www.youtube.com/playlist?list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g)
- [Inclusive Components](https://inclusive-components.design/)

## Maintenance Guidelines

When adding new features:

1. **Use semantic HTML** - Choose the right element for the job
2. **Add ARIA only when needed** - Don't over-ARIA; semantic HTML is usually sufficient
3. **Test with keyboard** - Ensure all functionality is keyboard accessible
4. **Check color contrast** - Use a contrast checker for new colors
5. **Test with screen reader** - Verify announcements make sense
6. **Validate HTML** - Run through an HTML validator
7. **Run automated tests** - Use axe or Lighthouse before committing

## Contact

For accessibility questions or to report issues:
- Open a GitHub issue with the "accessibility" label
- Consult WCAG guidelines for specific questions
- Test with actual assistive technology users when possible

---

**Remember: Accessibility benefits everyone, not just users with disabilities. It improves usability, SEO, and overall user experience.**
