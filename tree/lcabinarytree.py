struct TreeNode* lowestCommonAncestor( struct TreeNode* root, struct TreeNode *p, struct TreeNode* q )
{
    if(!p) return q; //corner case to accelerate from 16ms to 12ms;
    if(!q) return p;
    //the essential part: 1. p or q is the ancestor; 
    //2. p or q are in different sub-trees so the LCA will be in the higher level;
    if(!root || root == p || root == q) return root; 
    struct TreeNode *left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode *right = lowestCommonAncestor(root->right, p, q);
    if(left&&right) return root; //in different sub-trees;
    if(!left) return right; //in the same sub-tree;
    if(!right) return left;
}
