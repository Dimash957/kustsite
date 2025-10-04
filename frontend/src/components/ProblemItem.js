import React from 'react';

const ProblemItem = ({ item, isExpanded, onToggleExpanded }) => {
  const {
    title,
    description,
    evidence,
    impact,
    confidence,
    user_group,
    problem_category,
    source,
    timestamp
  } = item;

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      onToggleExpanded();
    }
  };

  const getConfidenceColor = (conf) => {
    if (conf >= 0.8) return 'high';
    if (conf >= 0.6) return 'medium';
    return 'low';
  };

  const formatConfidence = (conf) => {
    return `${Math.round(conf * 100)}%`;
  };

  return (
    <article className="problem-item" role="article">
      <header className="problem-item-header">
        <button
          className="problem-toggle"
          onClick={onToggleExpanded}
          onKeyDown={handleKeyDown}
          aria-expanded={isExpanded}
          aria-controls={`problem-content-${item.id}`}
          aria-label={`${isExpanded ? 'Collapse' : 'Expand'} details for ${title}`}
        >
          <h3 className="problem-title">{title}</h3>
          <span className="problem-toggle-icon" aria-hidden="true">
            {isExpanded ? '−' : '+'}
          </span>
        </button>
        
        <div className="problem-meta">
          <span className="problem-category" aria-label="Problem category">
            {problem_category}
          </span>
          <span className="problem-group" aria-label="User group">
            {user_group}
          </span>
          <span 
            className={`confidence-badge ${getConfidenceColor(confidence)}`}
            aria-label={`Confidence level: ${formatConfidence(confidence)}`}
          >
            {formatConfidence(confidence)}
          </span>
        </div>
      </header>

      <div 
        id={`problem-content-${item.id}`}
        className={`problem-content ${isExpanded ? 'expanded' : 'collapsed'}`}
        aria-hidden={!isExpanded}
      >
        {description && (
          <section className="problem-description">
            <h4>Description</h4>
            <p>{description}</p>
          </section>
        )}

        {evidence && (
          <section className="problem-evidence">
            <h4>Evidence</h4>
            <blockquote className="evidence-quote">
              "{evidence}"
            </blockquote>
          </section>
        )}

        {impact && (
          <section className="problem-impact">
            <h4>Impact</h4>
            <p>{impact}</p>
          </section>
        )}

        <footer className="problem-footer">
          {source && (
            <p className="problem-source">
              <strong>Source:</strong> {source}
            </p>
          )}
          {timestamp && (
            <p className="problem-timestamp">
              <strong>Analyzed:</strong> {new Date(timestamp).toLocaleDateString()}
            </p>
          )}
        </footer>
      </div>
    </article>
  );
};

export default ProblemItem;