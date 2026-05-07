const { execSync } = require('child_process');
const payload = {
    queries: [{ use_case: 'create github repository and push files' }],
    session: { generate_id: true }
};
const json = JSON.stringify(payload);
try {
    // In PowerShell/Windows, double quotes must be escaped as \"
    const command = `accio-mcp-cli call COMPOSIO_SEARCH_TOOLS --json "${json.replace(/"/g, '\\"')}"`;
    console.log(execSync(command).toString());
} catch (e) {
    console.log(e.stdout.toString());
}
