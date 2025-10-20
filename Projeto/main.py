# main.py
# Análise de Estresse Acadêmico - Script Completo
# =========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10

# =========================================================
# CONFIGURAÇÕES (OVERRIDE - ajuste aqui se necessário)
# =========================================================
STRESS_COL_OVERRIDE = None  # Ex: "Rate your academic stress index"
BAD_HABITS_COL_OVERRIDE = None  # Ex: "Do you have any bad habits"
STUDY_ENV_COL_OVERRIDE = None  # Ex: "Study Environment"
ACADEMIC_STAGE_COL_OVERRIDE = None  # Ex: "Academic Stage"
COPING_COL_OVERRIDE = None  # Ex: "What coping strategies do you use"

# =========================================================
# 1) LEITURA DO CSV COM FALLBACK DE ENCODINGS
# =========================================================
print("=" * 60)
print("ANÁLISE DE ESTRESSE ACADÊMICO")
print("=" * 60)

arquivo_csv = "academic Stress level - maintainance 1.csv"
df = None

for encoding in ['utf-8', 'latin1', 'cp1252']:
    try:
        df = pd.read_csv(arquivo_csv, encoding=encoding)
        print(f"\n✓ Arquivo lido com sucesso (encoding: {encoding})")
        print(f"✓ Total de registros: {len(df)}")
        break
    except:
        continue

if df is None:
    raise Exception("Não foi possível ler o arquivo CSV com nenhum dos encodings disponíveis.")

# Criar diretório de outputs
Path("outputs").mkdir(exist_ok=True)

# =========================================================
# 2) DETECÇÃO AUTOMÁTICA DE COLUNAS (FUZZY MATCHING)
# =========================================================
print("\n" + "=" * 60)
print("DETECTANDO COLUNAS...")
print("=" * 60)

def encontrar_coluna(df, palavras_chave, override=None):
    """Encontra coluna por palavras-chave com fuzzy matching"""
    if override:
        if override in df.columns:
            return override
        else:
            print(f"⚠ Override '{override}' não encontrado nas colunas.")
    
    for col in df.columns:
        col_lower = col.lower()
        for palavra in palavras_chave:
            if palavra.lower() in col_lower:
                return col
    return None

# Detectar colunas
stress_col = encontrar_coluna(df, ['stress', 'index', 'estresse'], STRESS_COL_OVERRIDE)
bad_habits_col = encontrar_coluna(df, ['bad habits', 'habits', 'maus hábitos'], BAD_HABITS_COL_OVERRIDE)
study_env_col = encontrar_coluna(df, ['study environment', 'environment', 'ambiente'], STUDY_ENV_COL_OVERRIDE)
academic_stage_col = encontrar_coluna(df, ['academic stage', 'stage', 'etapa'], ACADEMIC_STAGE_COL_OVERRIDE)
coping_col = encontrar_coluna(df, ['coping', 'strategies', 'estratégias'], COPING_COL_OVERRIDE)

# Mostrar colunas detectadas
print(f"\n✓ Coluna de Stress: {stress_col}")
print(f"✓ Coluna de Maus Hábitos: {bad_habits_col}")
print(f"✓ Coluna de Ambiente de Estudo: {study_env_col}")
print(f"✓ Coluna de Etapa Acadêmica: {academic_stage_col}")
print(f"✓ Coluna de Estratégias de Coping: {coping_col}")

# Verificar se encontrou as colunas principais
if not stress_col:
    print("\n⚠ ATENÇÃO: Coluna de stress não encontrada!")
    print("Configure STRESS_COL_OVERRIDE no início do código.")

# =========================================================
# 3) LIMPEZA E PREPARAÇÃO DOS DADOS
# =========================================================
print("\n" + "=" * 60)
print("LIMPEZA DOS DADOS...")
print("=" * 60)

# Remover duplicados
df_original = len(df)
df = df.drop_duplicates()
print(f"✓ Duplicados removidos: {df_original - len(df)}")

# Converter coluna de stress para numérico
def extrair_numero_stress(valor):
    """Extrai número do valor de stress"""
    if pd.isna(valor):
        return np.nan
    
    # Se já for número
    if isinstance(valor, (int, float)):
        return float(valor)
    
    # Converter para string e tentar extrair número
    texto = str(valor).lower().strip()
    
    # Mapeamento de textos ordinais
    mapa_ordinal = {
        'very low': 1, 'muito baixo': 1,
        'low': 2, 'baixo': 2,
        'medium': 3, 'médio': 3, 'moderate': 3,
        'high': 4, 'alto': 4,
        'very high': 5, 'muito alto': 5
    }
    
    # Verificar mapeamento ordinal
    for chave, valor in mapa_ordinal.items():
        if chave in texto:
            return float(valor)
    
    # Tentar extrair número do texto
    import re
    numeros = re.findall(r'\d+\.?\d*', texto)
    if numeros:
        return float(numeros[0])
    
    return np.nan

if stress_col:
    df['stress_numerico'] = df[stress_col].apply(extrair_numero_stress)
    valores_validos = df['stress_numerico'].notna().sum()
    print(f"✓ Valores de stress convertidos: {valores_validos} de {len(df)}")
else:
    print("⚠ Conversão de stress pulada (coluna não encontrada)")

print(f"\n✓ Dataset final: {len(df)} registros")

# =========================================================
# ANÁLISE 01: DISTRIBUIÇÃO DO ÍNDICE DE STRESS
# =========================================================
print("\n" + "=" * 60)
print("ANÁLISE 01: DISTRIBUIÇÃO DO ÍNDICE DE STRESS")
print("=" * 60)

if stress_col and 'stress_numerico' in df.columns:
    stress_dados = df['stress_numerico'].dropna()
    
    # Estatísticas descritivas
    print("\nESTATÍSTICAS DESCRITIVAS:")
    print(f"  Média: {stress_dados.mean():.2f}")
    print(f"  Mediana: {stress_dados.median():.2f}")
    print(f"  Desvio Padrão: {stress_dados.std():.2f}")
    print(f"  Mínimo: {stress_dados.min():.2f}")
    print(f"  Máximo: {stress_dados.max():.2f}")
    print(f"\nPERCENTIS:")
    print(f"  25%: {stress_dados.quantile(0.25):.2f}")
    print(f"  50%: {stress_dados.quantile(0.50):.2f}")
    print(f"  75%: {stress_dados.quantile(0.75):.2f}")
    
    # Criar gráficos
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histograma com KDE
    axes[0].hist(stress_dados, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0].set_xlabel('Índice de Stress')
    axes[0].set_ylabel('Frequência')
    axes[0].set_title('Distribuição do Índice de Stress')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Boxplot
    axes[1].boxplot(stress_dados, vert=True)
    axes[1].set_ylabel('Índice de Stress')
    axes[1].set_title('Boxplot do Índice de Stress')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/01_distribuicao_stress.png', dpi=300, bbox_inches='tight')
    print("\n✓ Gráfico salvo: outputs/01_distribuicao_stress.png")
    
    print("\n📊 INTERPRETAÇÃO:")
    print("A distribuição do estresse acadêmico mostra como os níveis de stress")
    print("estão distribuídos entre os estudantes. Uma média alta indica que a maioria")
    print("dos estudantes enfrenta níveis elevados de estresse acadêmico.")
    
else:
    print("⚠ Análise não realizada: coluna de stress não encontrada")

# =========================================================
# ANÁLISE 03: PROPORÇÃO DE MAUS HÁBITOS
# =========================================================
print("\n" + "=" * 60)
print("ANÁLISE 03: PROPORÇÃO DE MAUS HÁBITOS")
print("=" * 60)

if bad_habits_col:
    # Limpar e contar
    df[bad_habits_col] = df[bad_habits_col].astype(str).str.strip().str.lower()
    contagem = df[bad_habits_col].value_counts()
    
    # Calcular percentuais
    total = len(df)
    yes_count = contagem.get('yes', 0)
    no_count = contagem.get('no', 0)
    yes_pct = (yes_count / total) * 100
    no_pct = (no_count / total) * 100
    
    print(f"\nRESULTADOS:")
    print(f"  Sim (Yes): {yes_count} estudantes ({yes_pct:.1f}%)")
    print(f"  Não (No): {no_count} estudantes ({no_pct:.1f}%)")
    
    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 6))
    categorias = ['Sim', 'Não']
    valores = [yes_count, no_count]
    cores = ['#ff6b6b', '#51cf66']
    
    bars = ax.bar(categorias, valores, color=cores, edgecolor='black', alpha=0.7)
    ax.set_ylabel('Número de Estudantes')
    ax.set_title('Estudantes com Maus Hábitos')
    ax.grid(axis='y', alpha=0.3)
    
    # Adicionar percentuais nas barras
    for bar, valor, pct in zip(bars, valores, [yes_pct, no_pct]):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{valor}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('outputs/03_maus_habitos.png', dpi=300, bbox_inches='tight')
    print("\n✓ Gráfico salvo: outputs/03_maus_habitos.png")
    
    print("\n📊 INTERPRETAÇÃO:")
    print(f"Um total de {yes_pct:.1f}% dos estudantes reportaram ter maus hábitos.")
    print("Este é um indicador importante de comportamentos que podem afetar")
    print("o desempenho acadêmico e a saúde mental dos estudantes.")
    
else:
    print("⚠ Análise não realizada: coluna de maus hábitos não encontrada")

# =========================================================
# ANÁLISE 05: STRESS POR AMBIENTE DE ESTUDO
# =========================================================
print("\n" + "=" * 60)
print("ANÁLISE 05: STRESS POR AMBIENTE DE ESTUDO")
print("=" * 60)

if study_env_col and 'stress_numerico' in df.columns:
    # Calcular média por ambiente
    stress_por_ambiente = df.groupby(study_env_col)['stress_numerico'].agg(['mean', 'count', 'std'])
    stress_por_ambiente = stress_por_ambiente.sort_values('mean', ascending=False)
    
    print("\nMÉDIA DE STRESS POR AMBIENTE:")
    for ambiente, dados in stress_por_ambiente.iterrows():
        print(f"  {ambiente}: {dados['mean']:.2f} (n={int(dados['count'])}, DP={dados['std']:.2f})")
    
    print(f"\n🔴 MAIOR STRESS: {stress_por_ambiente.index[0]} ({stress_por_ambiente['mean'].iloc[0]:.2f})")
    print(f"🟢 MENOR STRESS: {stress_por_ambiente.index[-1]} ({stress_por_ambiente['mean'].iloc[-1]:.2f})")
    
    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(stress_por_ambiente.index, stress_por_ambiente['mean'], 
                   color='coral', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Média de Stress')
    ax.set_title('Nível Médio de Stress por Ambiente de Estudo')
    ax.grid(axis='x', alpha=0.3)
    
    # Adicionar valores nas barras
    for bar, valor in zip(bars, stress_por_ambiente['mean']):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f'{valor:.2f}',
                ha='left', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('outputs/05_stress_por_ambiente.png', dpi=300, bbox_inches='tight')
    print("\n✓ Gráfico salvo: outputs/05_stress_por_ambiente.png")
    
    print("\n📊 INTERPRETAÇÃO:")
    print("O ambiente de estudo tem impacto significativo no nível de estresse.")
    print("Ambientes com maior stress podem indicar condições inadequadas para estudo,")
    print("enquanto ambientes com menor stress podem oferecer melhores condições.")
    
else:
    print("⚠ Análise não realizada: colunas necessárias não encontradas")

# =========================================================
# ANÁLISE 07: RELAÇÃO ENTRE MAUS HÁBITOS E STRESS
# =========================================================
print("\n" + "=" * 60)
print("ANÁLISE 07: RELAÇÃO ENTRE MAUS HÁBITOS E STRESS")
print("=" * 60)

if bad_habits_col and 'stress_numerico' in df.columns:
    # Preparar dados
    df_analise = df[[bad_habits_col, 'stress_numerico']].copy()
    df_analise[bad_habits_col] = df_analise[bad_habits_col].str.lower().str.strip()
    df_analise = df_analise[df_analise[bad_habits_col].isin(['yes', 'no'])]
    df_analise = df_analise.dropna()
    
    # Estatísticas por grupo
    grupo_yes = df_analise[df_analise[bad_habits_col] == 'yes']['stress_numerico']
    grupo_no = df_analise[df_analise[bad_habits_col] == 'no']['stress_numerico']
    
    print("\nESTATÍSTICAS POR GRUPO:")
    print(f"  COM maus hábitos (Yes):")
    print(f"    Média: {grupo_yes.mean():.2f}")
    print(f"    Desvio Padrão: {grupo_yes.std():.2f}")
    print(f"    N: {len(grupo_yes)}")
    print(f"  SEM maus hábitos (No):")
    print(f"    Média: {grupo_no.mean():.2f}")
    print(f"    Desvio Padrão: {grupo_no.std():.2f}")
    print(f"    N: {len(grupo_no)}")
    
    # Teste t de Welch
    if len(grupo_yes) > 1 and len(grupo_no) > 1:
        t_stat, p_value = stats.ttest_ind(grupo_yes, grupo_no, equal_var=False)
        print(f"\nTESTE T (Welch):")
        print(f"  Estatística t: {t_stat:.4f}")
        print(f"  P-valor: {p_value:.4f}")
        
        if p_value < 0.05:
            print(f"  ✓ Diferença SIGNIFICATIVA (p < 0.05)")
        else:
            print(f"  ✗ Diferença NÃO significativa (p >= 0.05)")
    
    # Boxplot
    fig, ax = plt.subplots(figsize=(8, 6))
    data_plot = [grupo_no, grupo_yes]
    bp = ax.boxplot(data_plot, labels=['Sem Maus Hábitos', 'Com Maus Hábitos'],
                    patch_artist=True)
    
    # Colorir boxplots
    colors = ['#51cf66', '#ff6b6b']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_ylabel('Índice de Stress')
    ax.set_title('Comparação de Stress: Com vs Sem Maus Hábitos')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('outputs/07_maus_habitos_stress.png', dpi=300, bbox_inches='tight')
    print("\n✓ Gráfico salvo: outputs/07_maus_habitos_stress.png")
    
    print("\n📊 INTERPRETAÇÃO:")
    print("Esta análise investiga se estudantes com maus hábitos apresentam níveis")
    print("diferentes de estresse comparados aos sem maus hábitos. Um p-valor < 0.05")
    print("indica que a diferença é estatisticamente significativa.")
    
else:
    print("⚠ Análise não realizada: colunas necessárias não encontradas")

# =========================================================
# ANÁLISE 09: USO DE "EMOTIONAL BREAKDOWN" POR ETAPA ACADÊMICA
# =========================================================
print("\n" + "=" * 60)
print("ANÁLISE 09: USO DE 'EMOTIONAL BREAKDOWN' POR ETAPA")
print("=" * 60)

if coping_col and academic_stage_col:
    # Função para detectar emotional breakdown
    def tem_emotional_breakdown(texto):
        if pd.isna(texto):
            return False
        texto = str(texto).lower()
        palavras_chave = ['emotional', 'cry', 'crying', 'breakdown', 'chorar', 'choro']
        return any(palavra in texto for palavra in palavras_chave)
    
    # Aplicar detecção
    df['tem_breakdown'] = df[coping_col].apply(tem_emotional_breakdown)
    
    # Calcular percentuais por etapa
    resultado = df.groupby(academic_stage_col).agg(
        total=('tem_breakdown', 'count'),
        com_breakdown=('tem_breakdown', 'sum')
    )
    resultado['percentual'] = (resultado['com_breakdown'] / resultado['total']) * 100
    resultado = resultado.sort_values('percentual', ascending=False)
    
    print("\nPERCENTUAL DE USO POR ETAPA ACADÊMICA:")
    for etapa, dados in resultado.iterrows():
        print(f"  {etapa}: {dados['percentual']:.1f}% ({int(dados['com_breakdown'])}/{int(dados['total'])})")
    
    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(resultado.index, resultado['percentual'], 
                   color='mediumpurple', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Percentual (%)')
    ax.set_title('Uso de "Emotional Breakdown" como Estratégia de Coping por Etapa Acadêmica')
    ax.grid(axis='x', alpha=0.3)
    
    # Adicionar valores nas barras
    for bar, valor in zip(bars, resultado['percentual']):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f'{valor:.1f}%',
                ha='left', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('outputs/09_emotional_breakdown_por_etapa.png', dpi=300, bbox_inches='tight')
    print("\n✓ Gráfico salvo: outputs/09_emotional_breakdown_por_etapa.png")
    
    print("\n📊 INTERPRETAÇÃO:")
    print("Esta análise mostra qual percentual de estudantes em cada etapa acadêmica")
    print("utiliza 'emotional breakdown' (chorar, colapsos emocionais) como estratégia")
    print("de coping. Percentuais altos podem indicar níveis críticos de estresse.")
    
else:
    print("⚠ Análise não realizada: colunas necessárias não encontradas")

# =========================================================
# CONCLUSÃO E PRÓXIMOS PASSOS
# =========================================================
print("\n" + "=" * 60)
print("ANÁLISE COMPLETA!")
print("=" * 60)
print("\n📁 Todos os gráficos foram salvos na pasta 'outputs/'")
print("\n💡 PRÓXIMOS PASSOS SUGERIDOS:")
print("  1. Verificar a qualidade dos dados e possíveis outliers")
print("  2. Analisar correlações entre múltiplas variáveis")
print("  3. Realizar análise de regressão para prever níveis de stress")
print("  4. Investigar estratégias de coping mais efetivas")
print("  5. Comparar diferentes grupos demográficos (se houver dados)")
print("\n✓ Análise finalizada com sucesso!")