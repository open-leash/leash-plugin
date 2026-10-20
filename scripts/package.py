"""Build client-specific release archives without secrets, repositories or output files."""
from pathlib import Path
import json,sys,zipfile
root=Path(__file__).resolve().parents[1]
out=Path(sys.argv[1] if len(sys.argv)>1 else '/tmp/leash-plugin-packages')
out.mkdir(parents=True,exist_ok=True)
files=['plugin.json','mcp.json','.mcp.json','.claude-plugin/plugin.json','.cursor-plugin/plugin.json','.grok-plugin/plugin.json','gemini-extension.json','GEMINI.md','README.md','LICENSE','CHANGELOG.md','llms-install.md','assets/icon.png','skills/setup/SKILL.md','skills/leash/SKILL.md','rules/leash.mdc','openclaw.plugin.json','assets/icon-small.png']
for flavor in ['openai','portable','clawhub']:
 with zipfile.ZipFile(out/f'leash-{flavor}-1.0.1.zip','w',zipfile.ZIP_DEFLATED) as z:
  for path in files:
   content=(root/path).read_bytes()
   if path=='assets/icon.png' and flavor=='clawhub': content=(root/'assets/icon-small.png').read_bytes()
   if path=='mcp.json' and flavor=='openai':
    m=json.loads(content);m['mcpServers']['leash']['extensions']={'com.openai':{'auth':{'type':'oauth','client':{'mode':'dcr'},'baseScopes':['leash']}}};content=(json.dumps(m,indent=2)+'\n').encode()
   z.writestr(path,content)
 print(out/f'leash-{flavor}-1.0.1.zip')
