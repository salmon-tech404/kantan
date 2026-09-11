/**
 * Kantanda Mechanized Lint Rules
 * Automatically enforces static constraints without consuming LLM context tokens.
 */
module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended'
  ],
  rules: {
    // CODE-FUN-002: Function size <= 40 lines (excluding comments and blanks)
    'max-lines-per-function': ['error', { max: 40, skipBlankLines: true, skipComments: true }],
    
    // CODE-FUN-002: Cyclomatic depth / nesting <= 3
    'max-depth': ['error', 3],
    
    // FE-TS-001: Zero Any Policy
    '@typescript-eslint/no-explicit-any': 'error',
    
    // FE-TS-002: Strict Boolean / Equality Checks
    'eqeqeq': ['error', 'always'],
    
    // CODE-NAM-001: No cryptic single-letter variables (except i, j in loops)
    'id-length': ['error', { min: 2, exceptions: ['i', 'j', 'k', 'e', '_'] }],
    
    // Disallow console.log in production code (SEC-LOG-001)
    'no-console': ['warn', { allow: ['warn', 'error'] }]
  }
};
