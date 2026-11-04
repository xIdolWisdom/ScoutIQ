// ScoutIQ concept demo. Values are illustrative, not a live StatsBomb connection.
const players = [
  {name:'Michael Carrick',club:'Manchester United',role:'Central Midfielder',accuracy:86.62,progressive:24.39,score:90.22},
  {name:'John Obi Mikel',club:'Chelsea',role:'Defensive Midfielder',accuracy:90.95,progressive:19.25,score:83.28},
  {name:'Georginio Wijnaldum',club:'Newcastle United',role:'Attacking Midfielder',accuracy:83.47,progressive:13.05,score:82.47},
  {name:'Wes Hoolahan',club:'Norwich City',role:'Attacking Midfielder',accuracy:79.49,progressive:15.42,score:79.54},
  {name:'Ki Sung-yueng',club:'Swansea City',role:'Central Midfielder',accuracy:90.33,progressive:15.31,score:78.50},
  {name:'Mohamed Elneny',club:'Arsenal',role:'Defensive Midfielder',accuracy:92.07,progressive:16.67,score:78.03},
  {name:'Almen Abdi',club:'Watford',role:'Wide Midfielder',accuracy:79.80,progressive:13.04,score:69.48},
  {name:'Riyad Mahrez',club:'Leicester City',role:'Wide Midfielder',accuracy:69.51,progressive:16.01,score:56.47}
];
const $ = id => document.getElementById(id);
let selectedName = 'Michael Carrick';
function filteredPlayers(){const role=$('roleFilter').value;const q=$('playerSearch').value.trim().toLowerCase();return players.filter(p=>(role==='all'||p.role===role)&&(`${p.name} ${p.club}`.toLowerCase().includes(q)));}
function setProfile(p){selectedName=p.name;$('profileInitials').textContent=p.name.split(' ').map(w=>w[0]).slice(0,2).join('');$('profileName').textContent=p.name;$('profileClub').textContent=`${p.club} · ${p.role}`;$('profileAccuracy').textContent=`${p.accuracy.toFixed(2)}%`;$('profileProgressive').textContent=`${p.progressive.toFixed(2)}%`;$('profileScore').textContent=p.score.toFixed(2);$('accuracyMeter').style.width=`${p.accuracy}%`;$('progressMeter').style.width=`${Math.min(100,p.progressive*3)}%`;document.querySelectorAll('#playerTable tr').forEach(tr=>tr.classList.toggle('selected',tr.dataset.player===p.name));}
function renderPlayers(){const list=filteredPlayers().sort((a,b)=>b.score-a.score);$('playerCount').textContent=String(list.length).padStart(2,'0');$('avgAccuracy').textContent=list.length?(list.reduce((s,p)=>s+p.accuracy,0)/list.length).toFixed(1)+'%':'—';$('avgProgressive').textContent=list.length?(list.reduce((s,p)=>s+p.progressive,0)/list.length).toFixed(1)+'%':'—';$('topScore').textContent=list.length?list[0].score.toFixed(1):'—';$('topPlayer').textContent=list.length?list[0].name:'No players match';$('playerTable').replaceChildren();if(!list.length){const tr=document.createElement('tr');const td=document.createElement('td');td.colSpan=6;td.textContent='No matching players';tr.append(td);$('playerTable').append(tr);return;}for(const p of list){const tr=document.createElement('tr');tr.dataset.player=p.name;for(const value of [p.name,p.club,p.role,p.accuracy.toFixed(2)+'%',p.progressive.toFixed(2)+'%',p.score.toFixed(2)]){const td=document.createElement('td');td.textContent=value;if(value===p.score.toFixed(2))td.classList.add('score-cell');tr.append(td);}tr.addEventListener('click',()=>setProfile(p));$('playerTable').append(tr);}setProfile(list.find(p=>p.name===selectedName)||list[0]);}
$('roleFilter').addEventListener('change',renderPlayers);$('playerSearch').addEventListener('input',renderPlayers);renderPlayers();
$('year').textContent=new Date().getFullYear();
const menu=document.querySelector('.menu-toggle');
menu.addEventListener('click',()=>{const open=document.querySelector('nav').classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{document.querySelector('nav').classList.remove('open');menu.setAttribute('aria-expanded','false');}));
