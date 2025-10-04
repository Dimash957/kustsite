import React, { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar';
import FilterGroup from './components/FilterGroup';
import ProblemList from './components/ProblemList';
import { analyzeText, getGroups, getCategories } from './services/api';
import './styles/App.css';

function App() {
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedGroup, setSelectedGroup] = useState('People with disabilities');
  const [selectedCategory, setSelectedCategory] = useState('Accessibility');
  const [availableGroups, setAvailableGroups] = useState([]);
  const [availableCategories, setAvailableCategories] = useState([]);
  const [hasSearched, setHasSearched] = useState(false);

  // Load available groups and categories on mount
  useEffect(() => {
    const loadOptions = async () => {
      try {
        const [groups, categories] = await Promise.all([
          getGroups(),
          getCategories()
        ]);
        setAvailableGroups(groups);
        setAvailableCategories(categories);
      } catch (err) {
        console.error('Failed to load options:', err);
        // Set defaults if API fails
        setAvailableGroups(['People with disabilities', 'Elderly', 'Students']);
        setAvailableCategories(['Accessibility', 'Mobility', 'Cognitive', 'Mental health']);
      }
    };
    loadOptions();
  }, []);

  const handleSearch = async (query) => {
    if (!query.trim()) {
      setError('Please enter research text or abstract to analyze');
      return;
    }

    setLoading(true);
    setError(null);
    setHasSearched(true);

    try {
      const result = await analyzeText(query, selectedGroup, selectedCategory);
      setProblems(result.issues || []);
      
      if (!result.issues || result.issues.length === 0) {
        setError('No specific challenges identified in the provided text. Try different text or adjust filters.');
      }
    } catch (err) {
      setError('Failed to analyze text. Please try again. Error: ' + err.message);
      setProblems([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      {/* Main header with site purpose */}
      <header className="app-header" role="banner">
        <h1 className="site-title">Research Insights for Vulnerable Groups</h1>
        <p className="site-description">
          AI-powered synthesis of scientific research to identify and understand challenges 
          faced by vulnerable populations. Evidence-based insights made accessible.
        </p>
      </header>

      {/* Main content area */}
      <main id="main-content" className="main-content">
        {/* Search and analysis section */}
        <section className="search-section" aria-labelledby="search-heading">
          <h2 id="search-heading" className="visually-hidden">Search and Analyze Research</h2>
          
          <SearchBar 
            onSearch={handleSearch} 
            placeholder="Paste research abstract or text here..."
            disabled={loading}
          />

          {/* Filter controls */}
          <div className="filters-container" role="region" aria-label="Filter options">
            <FilterGroup 
              label="User Group" 
              id="user-group-filter"
              options={availableGroups} 
              value={selectedGroup} 
              onChange={setSelectedGroup}
              disabled={loading}
            />
            <FilterGroup 
              label="Problem Category" 
              id="category-filter"
              options={availableCategories} 
              value={selectedCategory} 
              onChange={setSelectedCategory}
              disabled={loading}
            />
          </div>
        </section>

        {/* Loading state */}
        {loading && (
          <div className="loading-state" role="status" aria-live="polite">
            <div className="spinner" aria-hidden="true"></div>
            <p>Analyzing research text with AI...</p>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className="error-message" role="alert" aria-live="assertive">
            <strong>Error:</strong> {error}
          </div>
        )}

        {/* Results section */}
        {!loading && hasSearched && !error && (
          <section className="results-section" aria-labelledby="results-heading">
            <h2 id="results-heading" className="results-title">
              Identified Challenges
              <span className="results-count" aria-label={`${problems.length} challenges found`}>
                ({problems.length} {problems.length === 1 ? 'challenge' : 'challenges'})
              </span>
            </h2>
            <div className="results-meta" aria-live="polite">
              Showing challenges for <strong>{selectedGroup}</strong> in <strong>{selectedCategory}</strong>
            </div>
            <ProblemList items={problems} />
          </section>
        )}

        {/* Empty state - before any search */}
        {!loading && !hasSearched && !error && (
          <section className="empty-state" aria-labelledby="welcome-heading">
            <h2 id="welcome-heading">How to Use This Platform</h2>
            <ol className="instructions-list">
              <li>
                <strong>Paste research text:</strong> Copy and paste an abstract or excerpt 
                from a research paper into the search box above.
              </li>
              <li>
                <strong>Select filters:</strong> Choose the user group and problem category 
                you're interested in exploring.
              </li>
              <li>
                <strong>Analyze:</strong> Click the search button to let AI extract relevant 
                challenges and present them in an accessible format.
              </li>
            </ol>
            <div className="info-box">
              <h3>About This Platform</h3>
              <p>
                This tool uses artificial intelligence to read scientific literature and 
                automatically extract key challenges faced by vulnerable populations. Our 
                goal is to make research findings more accessible and actionable for 
                communities, advocates, and policymakers.
              </p>
              <p>
                The platform follows WCAG accessibility guidelines to ensure everyone can 
                access and benefit from evidence-based insights.
              </p>
            </div>
          </section>
        )}
      </main>

      {/* Footer */}
      <footer className="app-footer" role="contentinfo">
        <p>
          Built with accessibility at its core. Following WCAG 2.1 Level AA standards.
        </p>
        <p>
          <small>
            AI-powered analysis may not capture all nuances. Always refer to original research for complete context.
          </small>
        </p>
      </footer>
    </div>
  );
}

export default App;
