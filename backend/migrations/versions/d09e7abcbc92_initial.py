"""initial

Revision ID: d09e7abcbc92
Revises: 
Create Date: 2025-03-10 14:35:09.819198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = 'd09e7abcbc92'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flashcard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sqlmodel.sql.sqltypes.AutoString(length=200), nullable=False),
    sa.Column('answer', sqlmodel.sql.sqltypes.AutoString(length=200), nullable=False),
    sa.Column('last_chosen_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchconditionnelpasse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchconditionnelpresent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchimperatifpasse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchimperatifpresent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatiffuturanterieur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatiffutursimple',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatifimparfait',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatifpasseanterieur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatifpassecompose',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatifpassesimple',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatifplusqueparfait',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchindicatifpresent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchsubjonctifimparfait',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchsubjonctifpasse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchsubjonctifplusqueparfait',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchsubjonctifpresent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('je', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('tu', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('il_elle', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('nous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vous', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('ils_elles', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('frenchverb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('infinitif', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('groupe', sa.Integer(), nullable=False),
    sa.Column('auxiliaire', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('indicatif_present_id', sa.Integer(), nullable=True),
    sa.Column('indicatif_imparfait_id', sa.Integer(), nullable=True),
    sa.Column('indicatif_passe_simple_id', sa.Integer(), nullable=True),
    sa.Column('indicatif_futur_simple_id', sa.Integer(), nullable=True),
    sa.Column('conditionnel_present_id', sa.Integer(), nullable=True),
    sa.Column('subjonctif_present_id', sa.Integer(), nullable=True),
    sa.Column('subjonctif_imparfait_id', sa.Integer(), nullable=True),
    sa.Column('imperatif_present_id', sa.Integer(), nullable=True),
    sa.Column('participe_present', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('indicatif_passe_compose_id', sa.Integer(), nullable=True),
    sa.Column('indicatif_plus_que_parfait_id', sa.Integer(), nullable=True),
    sa.Column('indicatif_passe_anterieur_id', sa.Integer(), nullable=True),
    sa.Column('indicatif_futur_anterieur_id', sa.Integer(), nullable=True),
    sa.Column('conditionnel_passe_id', sa.Integer(), nullable=True),
    sa.Column('subjonctif_passe_id', sa.Integer(), nullable=True),
    sa.Column('subjonctif_plus_que_parfait_id', sa.Integer(), nullable=True),
    sa.Column('imperatif_passe_id', sa.Integer(), nullable=True),
    sa.Column('participe_passe', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['conditionnel_passe_id'], ['frenchconditionnelpasse.id'], ),
    sa.ForeignKeyConstraint(['conditionnel_present_id'], ['frenchconditionnelpresent.id'], ),
    sa.ForeignKeyConstraint(['imperatif_passe_id'], ['frenchimperatifpasse.id'], ),
    sa.ForeignKeyConstraint(['imperatif_present_id'], ['frenchimperatifpresent.id'], ),
    sa.ForeignKeyConstraint(['indicatif_futur_anterieur_id'], ['frenchindicatiffuturanterieur.id'], ),
    sa.ForeignKeyConstraint(['indicatif_futur_simple_id'], ['frenchindicatiffutursimple.id'], ),
    sa.ForeignKeyConstraint(['indicatif_imparfait_id'], ['frenchindicatifimparfait.id'], ),
    sa.ForeignKeyConstraint(['indicatif_passe_anterieur_id'], ['frenchindicatifpasseanterieur.id'], ),
    sa.ForeignKeyConstraint(['indicatif_passe_compose_id'], ['frenchindicatifpassecompose.id'], ),
    sa.ForeignKeyConstraint(['indicatif_passe_simple_id'], ['frenchindicatifpassesimple.id'], ),
    sa.ForeignKeyConstraint(['indicatif_plus_que_parfait_id'], ['frenchindicatifplusqueparfait.id'], ),
    sa.ForeignKeyConstraint(['indicatif_present_id'], ['frenchindicatifpresent.id'], ),
    sa.ForeignKeyConstraint(['subjonctif_imparfait_id'], ['frenchsubjonctifimparfait.id'], ),
    sa.ForeignKeyConstraint(['subjonctif_passe_id'], ['frenchsubjonctifpasse.id'], ),
    sa.ForeignKeyConstraint(['subjonctif_plus_que_parfait_id'], ['frenchsubjonctifplusqueparfait.id'], ),
    sa.ForeignKeyConstraint(['subjonctif_present_id'], ['frenchsubjonctifpresent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('frenchverb')
    op.drop_table('frenchsubjonctifpresent')
    op.drop_table('frenchsubjonctifplusqueparfait')
    op.drop_table('frenchsubjonctifpasse')
    op.drop_table('frenchsubjonctifimparfait')
    op.drop_table('frenchindicatifpresent')
    op.drop_table('frenchindicatifplusqueparfait')
    op.drop_table('frenchindicatifpassesimple')
    op.drop_table('frenchindicatifpassecompose')
    op.drop_table('frenchindicatifpasseanterieur')
    op.drop_table('frenchindicatifimparfait')
    op.drop_table('frenchindicatiffutursimple')
    op.drop_table('frenchindicatiffuturanterieur')
    op.drop_table('frenchimperatifpresent')
    op.drop_table('frenchimperatifpasse')
    op.drop_table('frenchconditionnelpresent')
    op.drop_table('frenchconditionnelpasse')
    op.drop_table('flashcard')
    # ### end Alembic commands ###
