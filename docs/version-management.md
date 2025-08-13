# Version Management & Release Consistency

## 🚨 **CRITICAL RULE: Version-Tag Alignment**

**NEVER create a Git tag without first updating the project version in code.**

### **Mandatory Pre-Release Checklist**

Before creating ANY Git tag, you MUST:

1. **✅ Update version in `pyproject.toml`**
   ```toml
   [project]
   version = "X.Y.Z"  # Must match the tag you're about to create
   ```

2. **✅ Verify version consistency across all files**
   - `pyproject.toml` - Primary version source
   - `README.md` - If version is mentioned
   - Any other version references

3. **✅ Build and test the package**
   ```bash
   uv run python -m build
   # Verify dist/ contains correct version
   ls -la dist/
   ```

4. **✅ Commit version changes**
   ```bash
   git add .
   git commit -m "feat: Bump version to X.Y.Z"
   git push origin main
   ```

5. **✅ Create and push tag**
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

### **Version Naming Convention**

- **Format**: `vX.Y.Z` (e.g., `v0.2.1`, `v1.0.0`)
- **Must match**: `pyproject.toml` version exactly
- **No exceptions**: Never use different versions in code vs tags

### **Common Mistakes to Avoid**

❌ **WRONG**: Create tag `v0.2.1` with code version `0.2.0`
❌ **WRONG**: Update code version without rebuilding package
❌ **WRONG**: Push tag before committing version changes
❌ **WRONG**: Use different version formats (e.g., `v0.2.1` vs `0.2.1`)

✅ **CORRECT**: Update code → Build → Commit → Tag → Push

### **Release Workflow Validation**

The CI/CD pipeline expects:
- **Tag version** matches **package version**
- **Package builds successfully** with correct version
- **All validation steps pass** before PyPI upload

### **Emergency Fixes**

If you accidentally create a mismatched tag:

1. **Delete the tag locally and remotely**
   ```bash
   git tag -d vX.Y.Z
   git push origin --delete vX.Y.Z
   ```

2. **Fix the version in code**
3. **Rebuild the package**
4. **Commit and create correct tag**

### **Version Bumping Guidelines**

- **Patch** (`0.2.0` → `0.2.1`): Bug fixes, minor improvements
- **Minor** (`0.2.0` → `0.3.0`): New features, backward compatible
- **Major** (`0.2.0` → `1.0.0`): Breaking changes, major rewrites

### **Automated Checks (Future Enhancement)**

Consider implementing:
- Pre-commit hooks to validate version consistency
- CI checks to verify version matches tag
- Automated version bumping in release workflows

---

**Remember**: The release pipeline is triggered by tags, so version accuracy is critical for successful deployments!
