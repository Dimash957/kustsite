import axios from 'axios';

// API base URL - will use proxy in development
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 seconds timeout for AI processing
});

/**
 * Analyze research text to extract issues for a specific group and category
 * @param {string} text - Research text or abstract
 * @param {string} group - Target user group
 * @param {string} category - Problem category
 * @returns {Promise<Object>} Analysis results with issues array
 */
export async function analyzeText(text, group, category) {
  try {
    const response = await apiClient.post('/analyze', {
      text,
      group,
      category,
    });
    return response.data;
  } catch (error) {
    console.error('Error analyzing text:', error);
    throw new Error(
      error.response?.data?.error || 
      'Failed to analyze text. Please check your connection and try again.'
    );
  }
}

/**
 * Get comprehensive paper analysis
 * @param {string} text - Full research paper text
 * @returns {Promise<Object>} Comprehensive analysis
 */
export async function analyzePaper(text) {
  try {
    const response = await apiClient.post('/analyze-paper', { text });
    return response.data;
  } catch (error) {
    console.error('Error analyzing paper:', error);
    throw new Error(
      error.response?.data?.error || 
      'Failed to analyze paper. Please try again.'
    );
  }
}

/**
 * Get available user groups for filtering
 * @returns {Promise<Array<string>>} List of user groups
 */
export async function getGroups() {
  try {
    const response = await apiClient.get('/groups');
    return response.data.groups;
  } catch (error) {
    console.error('Error fetching groups:', error);
    // Return defaults on error
    return [
      'People with disabilities',
      'Elderly',
      'Students',
      'Children',
      'Low-income individuals'
    ];
  }
}

/**
 * Get available problem categories for filtering
 * @returns {Promise<Array<string>>} List of categories
 */
export async function getCategories() {
  try {
    const response = await apiClient.get('/categories');
    return response.data.categories;
  } catch (error) {
    console.error('Error fetching categories:', error);
    // Return defaults on error
    return [
      'Accessibility',
      'Mobility',
      'Cognitive',
      'Mental health',
      'Education',
      'Healthcare'
    ];
  }
}

/**
 * Health check endpoint
 * @returns {Promise<Object>} API health status
 */
export async function healthCheck() {
  try {
    const response = await apiClient.get('/health');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    return { status: 'unhealthy', error: error.message };
  }
}

export default apiClient;
