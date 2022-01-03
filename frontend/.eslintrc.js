module.exports = {
    extends: [
        'airbnb',
        'airbnb/hooks',
        'plugin:@typescript-eslint/recommended',
        'plugin:prettier/recommended',
        'next/core-web-vitals',
    ],
    parser: '@typescript-eslint/parser',
    // plugins: ['react', 'import', 'prettier'],
    rules: {
        //     '@typescript-eslint/no-empty-function': 'off',
        //     'no-restricted-syntax': 'off',
        //     'spaced-comment': 'off',
        //     'comma-dangle': ['error', 'always-multiline'],
        //     'arrow-parens': ['error', 'always'],
        //     'linebreak-style': 'off',
        //
        //     indent: 'off',
        //     'max-len': [
        //         'error',
        //         120,
        //         2,
        //         {
        //             ignoreUrls: true,
        //             ignoreComments: false,
        //             ignoreRegExpLiterals: true,
        //             ignoreStrings: true,
        //             ignoreTemplateLiterals: true,
        //         },
        //     ],
        //     'implicit-arrow-linebreak': 'off',
        //     'no-plusplus': 'off',
        //     'max-classes-per-file': 'off',
        //     'operator-linebreak': 'off',
        //     'object-curly-newline': 'off',
        //     'class-methods-use-this': 'off',
        //     'no-confusing-arrow': 'off',
        //     'function-paren-newline': 'off',
        //     'no-param-reassign': 'off',
        //     'no-shadow': 'warn',
        //     'space-before-function-paren': 'off',
        //     'consistent-return': 'off',
        //     'prettier': 'error',
        //
        //     '@typescript-eslint/explicit-function-return-type': 'off',
        //
        //     'react/prop-types': 'off',
        //     'react/static-property-placement': 'off',
        //     'react/state-in-constructor': 'off',
        'react/function-component-definition': 'off',
        'react/jsx-filename-extension': ['error', { extensions: ['.tsx'] }],
        //     'react/jsx-one-expression-per-line': 'off',
        //     'react/jsx-indent': ['error', 4],
        //     'react/jsx-indent-props': ['error', 4],
        'react/jsx-props-no-spreading': 'off',
        //     'react/destructuring-assignment': 'off',
        //     'react/sort-comp': 'off',
        //     'react/no-array-index-key': 'off',
        //
        //     'jsx-a11y/no-static-element-interactions': 'off',
        //     'jsx-a11y/click-events-have-key-events': 'off',
        //     'jsx-a11y/no-noninteractive-tabindex': 'off',
        //
        //     'import/prefer-default-export': 'off', // @grape: https://humanwhocodes.com/blog/2019/01/stop-using-default-exports-javascript-module/
        //     'import/order': [
        //         'error',
        //         {
        //             groups: [['builtin', 'external'], 'internal', 'parent', 'sibling', 'index'],
        //             'newlines-between': 'always',
        //         },
        //     ],
        //     'import/no-unresolved': 'off',
        //     'import/extensions': 'off',
        //     'import/no-extraneous-dependencies': ['off'], // можно включить тока нужно резолвы разрулить
        //     'arrow-body-style': 'off',
        //     'padding-line-between-statements': 'off',
        //     'no-unused-expressions': 'off',
        //
        //     'no-use-before-define': 'off',
        //     '@typescript-eslint/no-use-before-define': ['error'],
        // },
        // overrides: [
        //     {
        //         files: ['*.tsx?'],
        //         env: {
        //             browser: true,
        //         },
        //         globals: {
        //             window: true,
        //             document: true,
        //         },
        //     },
        // ],
        // settings: {
        //     react: {
        //         version: '17.0.2',
        //     },
    },
};
