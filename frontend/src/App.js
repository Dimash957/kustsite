import React, { useState, useEffect } from 'react';
import SearchBar from './components/SearchBar';
import FilterGroup from './components/FilterGroup';
import ProblemList from './components/ProblemList';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import { analyzeText, searchIssues, getCategories } from './services/api';
import './styles/App.css';

function App() {
  const [problems, setProblems] = useState([]);
  const [searchResults, setSearchResults] = useState([]);
  const [userGroup, setUserGroup] = useState('People with disabilities');
  const [problemCategory, setProblemCategory] = useState('Accessibility');
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [categories, setCategories] = useState({ user_groups: [], problem_categories: [] });
  const [activeTab, setActiveTab] = useState('analyze'); // 'analyze' or 'search'

  // Load categories on component mount
  useEffect(() => {
    const loadCategories = async () => {
      try {
        const data = await getCategories();
        setCategories(data);
      } catch (err) {
        console.error('Failed to load categories:', err);
      }
    };
    loadCategories();
  }, []);

  const handleAnalyze = async (text) => {
    if (!text.trim()) {
      setError('Please enter some text to analyze');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const result = await analyzeText(text, userGroup, problemCategory);
      setProblems(result.issues);
      setActiveTab('analyze');
    } catch (err) {
      setError(err.message || 'Analysis failed. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSearch = async (query, filters = {}) => {
    setIsLoading(true);
    setError(null);

    try {
      const result = await searchIssues(query, {
        user_group: filters.user_group || [userGroup],
        problem_category: filters.problem_category || [problemCategory]
      });
      setSearchResults(result.results);
      setActiveTab('search');
    } catch (err) {
      setError(err.message || 'Search failed. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleFilterChange = (filterType, value) => {
    if (filterType === 'userGroup') {
      setUserGroup(value);
    } else if (filterType === 'problemCategory') {
      setProblemCategory(value);
    }
  };

  return (
    <div className="App">
      <header className="App-header" role="banner">
        <h1>Research Insights for Vulnerable Groups</h1>
        <p className="App-description">
          Discover challenges and solutions from scientific literature using AI-powered analysis
        </p>
      </header>

      <main className="App-main" role="main">
        <nav className="App-nav" role="navigation" aria-label="Main navigation">
          <button
            className={`nav-button ${activeTab === 'analyze' ? 'active' : ''}`}
            onClick={() => setActiveTab('analyze')}
            aria-pressed={activeTab === 'analyze'}
            aria-describedby="analyze-description"
          >
            Analyze Research
          </button>
          <button
            className={`nav-button ${activeTab === 'search' ? 'active' : ''}`}
            onClick={() => setActiveTab('search')}
            aria-pressed={activeTab === 'search'}
            aria-describedby="search-description"
          >
            Search Issues
          </button>
        </nav>

        <div className="App-content">
          <div className="filters-section" role="region" aria-label="Filter options">
            <FilterGroup
              label="User Group"
              options={categories.user_groups}
              value={userGroup}
              onChange={(value) => handleFilterChange('userGroup', value)}
              type="radio"
              name="userGroup"
            />
            <FilterGroup
              label="Problem Category"
              options={categories.problem_categories}
              value={problemCategory}
              onChange={(value) => handleFilterChange('problemCategory', value)}
              type="radio"
              name="problemCategory"
            />
          </div>

          <div className="search-section" role="region" aria-label="Search and analysis">
            <SearchBar
              onAnalyze={handleAnalyze}
              onSearch={handleSearch}
              placeholder={activeTab === 'analyze' 
                ? "Paste research text or abstract to analyze..." 
                : "Search for specific issues..."
              }
              isLoading={isLoading}
              mode={activeTab}
            />
          </div>

          {error && <ErrorMessage message={error} onDismiss={() => setError(null)} />}

          {isLoading && <LoadingSpinner />}

          <div className="results-section" role="region" aria-label="Analysis results">
            {activeTab === 'analyze' && problems.length > 0 && (
              <ProblemList 
                items={problems} 
                title={`Issues Found for ${userGroup} in ${problemCategory}`}
                emptyMessage="No issues found. Try adjusting your filters or analyzing different text."
              />
            )}

            {activeTab === 'search' && searchResults.length > 0 && (
              <ProblemList 
                items={searchResults} 
                title="Search Results"
                emptyMessage="No results found. Try different search terms or filters."
              />
            )}

            {!isLoading && activeTab === 'analyze' && problems.length === 0 && (
              <div className="empty-state" role="status" aria-live="polite">
                <p>Enter research text above to analyze and discover relevant issues.</p>
              </div>
            )}

            {!isLoading && activeTab === 'search' && searchResults.length === 0 && (
              <div className="empty-state" role="status" aria-live="polite">
                <p>Enter search terms above to find relevant issues.</p>
              </div>
            )}
          </div>
        </div>
      </main>

      <footer className="App-footer" role="contentinfo">
        <p>
          This platform uses AI to analyze research literature and identify challenges faced by vulnerable groups.
          Results are generated automatically and should be verified for accuracy.
        </p>
      </footer>
    </div>
  );
}

export default App;