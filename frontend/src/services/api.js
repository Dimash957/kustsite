import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000, // 30 seconds timeout for AI processing
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to ${config.url}`);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('API Error:', error);
    
    if (error.response) {
      // Server responded with error status
      const message = error.response.data?.error || `Server error: ${error.response.status}`;
      throw new Error(message);
    } else if (error.request) {
      // Request was made but no response received
      throw new Error('Network error: Unable to connect to server');
    } else {
      // Something else happened
      throw new Error(error.message || 'An unexpected error occurred');
    }
  }
);

export const analyzeText = async (text, userGroup, problemCategory) => {
  try {
    const response = await api.post('/analyze', {
      text,
      user_group: userGroup,
      problem_category: problemCategory,
    });
    
    return response.data;
  } catch (error) {
    throw new Error(error.message || 'Failed to analyze text');
  }
};

export const searchIssues = async (query, filters = {}) => {
  try {
    const response = await api.post('/search', {
      query,
      filters,
    });
    
    return response.data;
  } catch (error) {
    throw new Error(error.message || 'Failed to search issues');
  }
};

export const getCategories = async () => {
  try {
    const response = await api.get('/categories');
    return response.data;
  } catch (error) {
    throw new Error(error.message || 'Failed to load categories');
  }
};

export const healthCheck = async () => {
  try {
    const response = await api.get('/health');
    return response.data;
  } catch (error) {
    throw new Error(error.message || 'Health check failed');
  }
};

export default api;